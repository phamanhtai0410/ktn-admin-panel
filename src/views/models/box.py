from gettext import gettext

from flask import flash
from flask_admin.form import Select2Widget
from markupsafe import Markup
from wtforms import HiddenField, SelectField

from src.abis import factory_abi, box_creator_abi
from src.config import Config
from src.models.nft_collection import NftCollection
from src.models.nft_detail import NftDetail
from src.views.base import MyBaseModelView, RowActionListMixin


class BoxView(MyBaseModelView, RowActionListMixin):
    column_list = ['name', 'address', 'price', 'collection', 'nfts', 'active', 'created_time']
    # create_modal = True
    # edit_template = 'form.abi.create_from.html'
    edit_template = 'form/models/box/edit.html'
    # form_columns = ['collection_id', 'name', 'description','image', 'nfts']
    can_delete = False
    can_create = False
    # edit_modal = True
    can_view_details = True
    form_overrides = dict(collection=SelectField
                          )
    form_subdocuments = {

    }
    form_args = {
    }

    def image_format(view, context, model, name):
        # _image = model['image']
        return Markup(f'<a target="_blank" href="{model["image"]}"> image </a>')

    def get_nfts(self):
        return NftDetail.objects()

    def create_form(self, obj=None):
        self.form_widget_args = {}
        _form = super(BoxView, self).create_form(obj)
        _cols = NftCollection.objects()

        _form.collection.choices = [(x.address, x.name) for x in _cols]
        # _form.rarity_nfts.data = None
        return _form

    def edit_form(self, obj=None):
        self.form_widget_args = {
            'address': {
                'readonly': True
            },
            'collection': {
                'readonly': True
            }
        }
        _form = super(BoxView, self).edit_form(obj)
        _cols = NftCollection.objects()

        self.before_price = obj.price

        _form.collection.choices = [(x.address, x.name) for x in _cols]
        return _form

    column_searchable_list = ['name']

    column_default_sort = ('created_time', True)
    column_formatters = {
        'image': image_format
    }

    def render(self, template, **kwargs):
        kwargs['creator_abi'] = box_creator_abi
        kwargs['creator_address'] = Config.BOX_CREATOR_ADDRESS

        kwargs['before_price'] = 0
        if hasattr(self, 'before_price'):
            kwargs['before_price'] = self.before_price

        return super(BoxView, self).render(template, **kwargs)
