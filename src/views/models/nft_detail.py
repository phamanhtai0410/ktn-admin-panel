from gettext import gettext

from flask import flash, redirect
from markupsafe import Markup
from pydash import get

from src.connect import bsc
from src.views.base import MyBaseModelView

from wtforms import validators

class NftDetailView(MyBaseModelView):
    column_list = ['nft_id', 'name', 'type', 'rarity', 'description', 'image', 'price', 'is_show', 'created_time']
    can_edit = True
    can_create = True
    can_delete = True
    # column_editable_list = ['price', 'is_show']
    edit_modal = True

    def image_format(view, context, model, name):
        # _image = model['image']
        return Markup(f'<a target="_blank" href="{model["image"]}"> image </a>')

    column_searchable_list = ['name']

    column_filters = ['type']

    column_default_sort = ('created_time', True)
    column_formatters = {
        'image': image_format
    }

    def on_model_change(self, form, model, is_created):
        try:
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
                    raise Exception( f"Failed: Update tx {_tx_hash}. Please re-check.")

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
                    raise Exception( f"Failed: Update tx {_tx_hash}. Please re-check.")
                # pass

        except Exception as e:
            # flash(gettext(f'{e}'), 'error')
            raise validators.ValidationError(e)
            # return redirect(self.get_url('.index_view'))


    def create_form(self, obj=None):
        self.form_widget_args = {}
        return super(NftDetailView, self).edit_form(obj)

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

        return super(NftDetailView, self).edit_form(obj)
