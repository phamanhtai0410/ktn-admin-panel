from gettext import gettext

import requests
from flask import flash, request, url_for
from flask_admin.form import Select2Widget
from flask_admin.model.template import EditRowAction
from markupsafe import Markup
from wtforms import HiddenField

from src.abis import factory_abi, royalty_controller_abi
from src.config import Config
from src.models.nft_collection import NftCollection
from src.models.nft_mesh import Mesh
from src.models.royalty import Royalty
from src.views.base import MyBaseModelView, RowActionListMixin
from src.utils.s3_image_uploader import S3ImageUploadField
from src.utils.s3_3d_models_uploader import S3_3D_ModelUploadField
from wtforms.fields import SelectMultipleField


def get_nfts_options():
    return [(f'{x.mesh_id}', x.name) for x in Mesh.objects()]


class NftCollectionView(MyBaseModelView, RowActionListMixin):
    column_list = ['collection_id', 'name', 'symbol',
                   'address', 'description', 'types_list', 'chain', 'is_box', 'created_time']
    # create_modal = True
    edit_template = 'form/models/factory/edit.html'
    create_modal_template = 'form/models/factory/modals/create.html'
    create_template = 'form/models/factory/create.html'
    details_template = "form/models/factory/details.html"
    list_template = 'custom/menu_bar_nft.html'

    # form_columns = ['collection_id', 'name', 'description','image', 'nfts']
    can_delete = False
    can_view_details = True
    # edit_modal = True
    can_create = False
    column_labels = {
        'collection_id': 'Id'
    }
    #
    # def royalty_format(self, context, model, name):
    #     _royalty = Royalty.objects(collection_address=model['address'])
    #     permission = '<ul>'
    #     for item in _royalty:
    #         permission += f'<li href="#" target="_blank" >{item.user_address} - {item.percent}</li>'
    #     permission += f'<li ><a href="{url_for("royalty.create_view", collection_address=model["address"])}"><i class="fa fa-plus-circle" aria-hidden="true"></i></a></li>'
    #     return Markup(permission + "</ul>")

    form_overrides = dict(
        nfts=SelectMultipleField,
        collection_id=HiddenField,
        # rarity_nfts=HiddenField,
        address=HiddenField,
        image=S3ImageUploadField,
        max_rarity=HiddenField,
        block_number=HiddenField,
        box_image_url=S3ImageUploadField
    )
    form_subdocuments = {
        'types_list': {
            'form_subdocuments': {
                None: {
                    'form_overrides': dict(
                        ImageUrl=S3ImageUploadField,
                        AnimationModelUrl=S3_3D_ModelUploadField
                    )
                }
            }
        }
    }

    form_args = {
        'nfts': {
            'choices': [],
            'widget': Select2Widget(multiple=True)
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

    # def types_list_format(view, context, model, name):
    #     print("*** DEBUG : model = ", model)
    #     _display = '<ul>'
    #     for _item in model:
    #         _display += f'<li><pre>             \
    #             {_item["AssetID"]}              \
    #             {_item["DataTableID"]}          \
    #             {_item["AssetRarity"]}          \
    #             {_item["rate"]}                 \
    #             {_item["AssetRarity"]}          \
    #             {_item["ImageUrl"]}             \
    #             {_item["AnimationModelUrl"]}    \
    #         </pre></li>'

    #     return Markup(
    #         _display + '</ul>'
    #     )

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
            },
            'treasury_address': {
                'type': 'button',
                "value": 'Connect wallet',
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
                'readonly': False
            },
            'symbol': {
                'readonly': False
            },
            'royalty_rate': {
                'readonly': False
            },
            'total_supply': {
                'readonly': False
            },
            'types_list': {
                'readonly': True
            },
            'treasury_address': {
                # 'type': 'button',
                "placeholder": 'Connect wallet',
                "we3-address": "input_address",
                "readonly": True
            },
            'deployed': {
                'disabled': True
            },
            'chain_id': {
                'disabled': True
            },
            'chain': {
                'disabled': True
            },
            'pay_token_address': {
                'disabled': True
            },
            'dapp_creator_address': {
                'disabled': True
            }
        }

        self.before_disable_mint = obj.disable_mint
        self.before_royalty = obj.royalty

        _form = super(NftCollectionView, self).edit_form(obj)
        _form.block_number.data = 0
        return _form

    # def details_view(self, obj=None):
    #     _view = super(NftCollectionView, self).details_view(obj)
    #     return _view

    # def get_save_return_url(self, model, is_created):
    #     return self.get_url('.details_view', id=model.id)

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
        'image': image_format,
        # 'royalty': royalty_format,
        # 'types_list': types_list_format
    }

    def render(self, template, **kwargs):
        kwargs['factory_abi'] = factory_abi
        kwargs['royalty_controller_abi'] = royalty_controller_abi
        kwargs['factory_address'] = Config.NFT_FACTORY_ADDRESS
        kwargs['royalty_controller_address'] = Config.ROYALTY_CONTROLLER_ADDRESS
        kwargs['before_disable_mint'] = 0
        if hasattr(self, 'before_disable_mint'):
            kwargs['before_disable_mint'] = self.before_disable_mint
        kwargs['before_royalty'] = []
        if hasattr(self, 'before_disable_mint'):
            kwargs['before_royalty'] = self.before_royalty
        kwargs['nft_chain_supported'] = Config.NFT_CHAIN_SUPPORTED
        return super(NftCollectionView, self).render(template, **kwargs)

    def create_model(self, form):
        try:
            return super(NftCollectionView, self).create_model(form)
        except Exception as e:
            flash(gettext(str(e)), 'error')

    def _can_edit(self, model):

        # Put your logic here to allow edit per model
        # return True to allow edit
        return not model.deployed

    def allow_row_action(self, action, model):
        print("allow_row_action", action, model)

        # # Deal with Edit Action
        if isinstance(action, EditRowAction):
            return self._can_edit(model)

        # # Deal with Delete Action
        # if isinstance(action, DeleteRowAction):
        #     return self._can_delete(model)

        # # Deal with other actions etc

        # otherwise whatever the inherited method returns
        return super().allow_row_action(action, model)
