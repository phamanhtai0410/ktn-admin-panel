import traceback
from gettext import gettext
from flask_admin.form import Select2Widget

from flask import flash, redirect
from markupsafe import Markup
from mongoengine.queryset.base import BaseQuerySet
from pydash import get, find
from wtforms.fields.core import UnboundField, SelectField

from src.connect import bsc
from src.models.nft_type import NftType
from src.views.base import MyBaseModelView
from src.utils.s3_image_uploader import s3ImageUploadField

from wtforms import validators


class NftDetailView(MyBaseModelView):
    column_list = ['nft_id', 'name', 'type', 'rarity', 'description',
                   'image', 'price', 'discount', 'commission',
                   'is_show', 'created_time']
    can_edit = True
    can_create = True
    can_delete = True
    # column_editable_list = ['price', 'is_show']
    edit_modal = True
    create_modal = True
    can_view_details = True
    form_args = {}
    form_overrides = dict(
        type=SelectField,
        image=s3ImageUploadField
    )

    def image_format(view, context, model, name):
        return Markup(f'<a target="_blank" href="{model["image"]}"> image </a>')

    def format_type(view, context, model, name):
        _type = find(view.get_type_options(), lambda x: int(x[0]) == model['type'])
        if _type:
            return _type[1]
        return model['type']

    column_searchable_list = ['name']

    column_filters = ['type']

    column_default_sort = ('created_time', True)
    column_formatters = {
        'image': image_format,
        'type': format_type
    }

    def get_type_options(self):
        return [(f'{x.type_id}', x.name) for x in NftType.objects()]

    def scaffold_form(self):
        print("scaffold_form here", )
        self.form_args = {
            'type': {
                'choices': [],
                'widget': Select2Widget(multiple=False)
            }
        }
        _form = super(NftDetailView, self).scaffold_form()
        _form.type.kwargs['choices'] = self.form_args['type']['choices']
        _form.image.kwargs['base_path'] = "/admin/static"
        return _form

    def on_model_change(self, form, model, is_created):
        try:

            _type = NftType.objects(type_id=form.type.data)
            print('_type_type_type')
            if _type and _type[0]:
                _type = _type[0]
            else:
                raise Exception("Not found type")
            if _type.max_rarity < form.rarity.data:
                raise Exception(f"Invalid rarity: must be < {_type.max_rarity}")
            if is_created:
                max_rarity = bsc.smc_nft.functions.getMaxRarityValue(
                    bsc.toInt(text=str(form.type.data))
                ).call()
                print("max", max_rarity)
                if max_rarity < form.rarity.data:
                    raise Exception(f"[On chain]Invalid rarity: must be < {max_rarity}")
                # raise Exception(max_rarity)

            else:
                print(self.before_price)
                print(form.price.data)
                print('form.is_show.data', form.is_show.data, self.before_is_show)

                if self.before_price != form.price.data:
                    tx = bsc.smc_creator.functions.updatePrice(
                        bsc.toInt(text=str(form.type.data)),
                        bsc.toInt(text=str(form.rarity.data)),
                        bsc.toWei(form.price.data, unit='ether')
                    ).buildTransaction({
                        'gasPrice': bsc.eth.gas_price,
                        'nonce': bsc.eth.getTransactionCount(bsc.my_account.address)
                    })
                    signed_tx = bsc.my_account.signTransaction(tx)
                    _txn = bsc.eth.send_raw_transaction(signed_tx.rawTransaction)

                    _tx_hash = _txn.hex()
                    _txn_receipt = bsc.eth.wait_for_transaction_receipt(_tx_hash)
                    print(f"Log tx hash: {_tx_hash}")
                    if get(_txn_receipt, 'status') != 1:
                        raise Exception(f"Failed: Update tx {_tx_hash}. Please re-check.")

                if self.before_is_show != form.is_show.data:
                    _force_price = form.price.data
                    if not form.is_show.data:
                        _force_price = 10000000

                    tx = bsc.smc_creator.functions.updatePrice(
                        bsc.toInt(text=str(form.type.data)),
                        bsc.toInt(text=str(form.rarity.data)),
                        bsc.toWei(_force_price, unit='ether')
                    ).buildTransaction({
                        'gasPrice': bsc.eth.gas_price,
                        'nonce': bsc.eth.getTransactionCount(bsc.my_account.address)
                    })
                    signed_tx = bsc.my_account.signTransaction(tx)
                    _txn = bsc.eth.send_raw_transaction(signed_tx.rawTransaction)
                    _tx_hash = _txn.hex()
                    print("_tx_hash", _tx_hash)
                    print(f"Log tx hash: {_tx_hash}")
                    _txn_receipt = bsc.eth.wait_for_transaction_receipt(_tx_hash)

                    if get(_txn_receipt, 'status') != 1:
                        raise Exception(f"Failed: Update tx {_tx_hash}. Please re-check.")
                    # pass

        except Exception as e:
            # flash(gettext(f'{e}'), 'error')
            traceback.print_exc()
            raise validators.ValidationError(e)
            # return redirect(self.get_url('.index_view'))

    def create_form(self, obj=None):
        self.form_widget_args = {}
        _form =  super(NftDetailView, self).create_form(obj)
        _form.type.choices = self.get_type_options()
        return _form

    def edit_form(self, obj=None):
        try:

            self.form_widget_args = {
                'type': {
                    'disabled': True
                },
                'rarity': {
                    'disabled': True
                }
            }

            self.before_is_show = obj.is_show

            self.before_price = obj.price
        except AttributeError:
            pass
        _form = super(NftDetailView, self).edit_form(obj)
        _form.type.choices = self.get_type_options()
        return _form

    def lock_admin(self):
        return True
