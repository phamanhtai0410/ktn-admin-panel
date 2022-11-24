from gettext import gettext

import requests
from flask import flash, request
from flask_admin.form import Select2Widget
from markupsafe import Markup
from wtforms import HiddenField

from src.abis import factory_abi
from src.config import Config
from src.models.nft_collection import NftCollection
from src.models.nft_mesh import Mesh
from src.views.base import MyBaseModelView, RowActionListMixin
from src.utils.s3_image_uploader import S3ImageUploadField

from wtforms.fields import SelectMultipleField


def get_nfts_options():
    return [(f'{x.mesh_id}', x.name) for x in Mesh.objects()]


class NftCollectionView(MyBaseModelView, RowActionListMixin):
    column_list = ['collection_id', 'name', 'symbol', 'address', 'description', 'created_time']
    # create_modal = True
    # edit_template = 'form.abi.create_from.html'
    create_modal_template = 'form/models/factory/modals/create.html'
    create_template = 'form/models/factory/create.html'
    # form_columns = ['collection_id', 'name', 'description','image', 'nfts']
    can_delete = False
    # edit_modal = True
    column_labels = {
        'collection_id': 'Id'
    }

    form_overrides = dict(nfts=SelectMultipleField,
                          collection_id=HiddenField,
                          # rarity_nfts=HiddenField,
                          address=HiddenField,
                          image=S3ImageUploadField,
                          max_rarity=HiddenField,
                          block_number=HiddenField
                          )
    form_subdocuments = {

    }
    form_args = {
        'nfts': {
            'choices': [],
            'widget': Select2Widget(multiple=True)
        }
    }
    form_widget_args = {
        'collection_id': {
        }
    }

    def on_model_change(self, form, model, is_created):
        if is_created:
            print({
                "contract": form.address.data,
                "type": "NFT",
                "from_block": form.block_number.data
            })
            res = requests.post(f'{Config.SMC_IAPI}/background_jobs', json={
                "contract": form.address.data,
                "type": "NFT",
                "from_block": form.block_number.data
            }, timeout=10)
            print(res.text)

    def title(self):
        return "OKe lk"

    def image_format(view, context, model, name):
        # _image = model['image']
        return Markup(f'<a target="_blank" href="{model["image"]}"> image </a>')

    def scaffold_form(self):
        self.form_args = {
            'nfts': {
                'choices': [],
                'widget': Select2Widget(multiple=True)
            }
        }
        return super(NftCollectionView, self).scaffold_form()

    def get_nfts(self):
        return Mesh.objects()

    def create_form(self, obj=None):
        self.form_args = {
            'nfts': {
                'choices': [],
                'widget': Select2Widget(multiple=True)
            }
        }
        self.form_widget_args = {
            'collection_id': {
                'readonly': True
            },
            'nfts': {
                'readonly': True
            },
            'max_rarity': {
                'readonly': True
            }
        }
        _form = super(NftCollectionView, self).create_form(obj)
        _cols = NftCollection.objects()

        _max_id = 0

        if _cols:
            _max_id = max([col.collection_id for col in _cols]) or 0

        _form.collection_id.data = _max_id + 1
        # _form.rarity_nfts.data = None
        return _form

    def edit_form(self, obj=None):

        self.form_widget_args = {
            'name': {
                'readonly': True
            },
            'symbol': {
                'readonly': True
            }
        }

        self.before_delist = obj.delist

        _form = super(NftCollectionView, self).edit_form(obj)
        return _form

    def get_nfts_options(self):
        self.form_args = {
            'nfts': {
                'choices': [],
                'widget': Select2Widget(multiple=True)
            }
        }
        return [(f'{x.mesh_id}', x.name) for x in Mesh.objects()]

    column_searchable_list = ['name']

    column_default_sort = ('created_time', True)
    column_formatters = {
        'image': image_format
    }

    def render(self, template, **kwargs):
        kwargs['factory_abi'] = factory_abi
        kwargs['factory_address'] = Config.NFT_FACTORY_ADDRESS
        kwargs['before_delist'] = 0
        if hasattr(self, 'before_delist'):
            kwargs['before_delist'] = self.before_delist

        return super(NftCollectionView, self).render(template, **kwargs)

    def create_model(self, form):
        try:
            return super(NftCollectionView, self).create_model(form)
        except Exception as e:
            flash(gettext(str(e)), 'error')
