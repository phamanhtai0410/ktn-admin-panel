from gettext import gettext

import requests
from flask import flash, url_for
from flask_admin.contrib.mongoengine.fields import ModelFormField
from flask_admin.form import FormOpts
from markupsafe import Markup
from wtforms import HiddenField, SelectField, FieldList, Form, IntegerField, validators

from src.abis import factory_abi, box_creator_abi, box_factory_abi
from src.config import Config
from src.models.box import Box
from src.models.box_rate import RateOfBox
from src.models.nft_collection import NftCollection
from src.models.mesh_material import MeshMaterial
from src.utils.s3_image_uploader import S3ImageUploadField
from src.views.base import MyBaseModelView, RowActionListMixin


class BoxView(MyBaseModelView, RowActionListMixin):
    column_list = ['name', 'address', 'price', 'collection', 'rates', 'active', 'created_time']
    # create_modal = True
    # edit_template = 'form.abi.create_from.html'
    edit_template = 'form/models/box/edit.html'
    create_template = 'form/models/box/create.html'
    def rate_format(self, context, model, name):
        _variables = RateOfBox.objects(box_id=model['box_id'])
        permission = '<ul>'
        for item in _variables:
            permission += f'<li  ><a href="{url_for("rateofbox.details_view", id=item["id"])}"> Rarity {item.rarity} ; Mesh index {item.mesh_index} ; Mesh material {item.mesh_material} = {item.proportion}% </a> </li>'
        permission += f'<li ><a href="{url_for("rateofbox.create_view", box_id=model["box_id"])}"><i class="fa fa-plus-circle" aria-hidden="true"></i></a></li>'
        return Markup(permission + "</ul>")

    # form_columns = ['collection_id', 'name', 'description','image', 'nfts']
    can_delete = False
    can_create = True
    # edit_modal = True
    can_view_details = True
    
    form_overrides = dict(
        collection=SelectField,
        image=S3ImageUploadField,
        address=HiddenField,
        block_number=HiddenField,
        box_id=HiddenField,
        cid=HiddenField
    )

    def image_format(view, context, model, name):
        # _image = model['image']
        return Markup(f'<a target="_blank" href="{model["image"]}"> image </a>')

    def get_nfts(self):
        return MeshMaterial.objects()

    def create_form(self, obj=None):
        self.form_widget_args = {}
        _form = super(BoxView, self).create_form(obj)
        _cols = NftCollection.objects()
        _boxes = Box.objects()
        _max_id = 0
        if _boxes:
            _max_id = max([col.box_id for col in _boxes]) or 0
        _form.box_id.data = _max_id + 1

        _form.collection.choices = [(x.address, x.name) for x in _cols]

        return _form

    def edit_form(self, obj=None):
        self.form_widget_args = {
            'address': {
                'readonly': True
            },
            'collection': {
                'readonly': True
            },
            'box_id': {
                'readonly': True
            },
            'total_supply': {
                'readonly': True
            },
            'royalty_rate': {
                'readonly': True
            }
        }
        _form = super(BoxView, self).edit_form(obj)
        _cols = NftCollection.objects()

        self.before_price = obj.price
        self.before_disable_mint = obj.disable_mint
        _form.collection.choices = [(x.address, x.name) for x in _cols]
        return _form

    column_searchable_list = ['name']

    column_default_sort = ('created_time', True)
    column_formatters = {
        'image': image_format,
        'rates': rate_format
    }

    def on_model_change(self, form, model, is_created):
        if is_created:
            res = requests.post(f'{Config.SMC_IAPI}/background_jobs', json={
                "contract": form.address.data,
                "type": "BOX",
                "from_block": form.block_number.data
            }, timeout=10)
            print(res.text)

    def render(self, template, **kwargs):

        kwargs['creator_abi'] = box_creator_abi
        kwargs['creator_address'] = Config.BOX_CREATOR_ADDRESS


        kwargs['factory_abi'] = box_factory_abi
        kwargs['factory_address'] = Config.BOX_FACTORY_ADDRESS
        kwargs['pay_token'] = Config.PAY_TOKEN
        kwargs['before_price'] = 0

        kwargs['before_disable_mint'] = False

        kwargs['nft_factory_abi'] = factory_abi
        kwargs['nft_factory_address'] = Config.NFT_FACTORY_ADDRESS

        if hasattr(self, 'before_price'):
            kwargs['before_price'] = self.before_price

        if hasattr(self, 'before_disable_mint'):
            kwargs['before_disable_mint'] = self.before_disable_mint

        return super(BoxView, self).render(template, **kwargs)
