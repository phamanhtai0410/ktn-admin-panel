import uuid
from markupsafe import Markup
from wtforms.fields.core import SelectField

from src.abis import factory_abi
from src.config import Config
from src.models.nft_collection import NftCollection
from src.models.nft_detail import NftDetail
from src.models.nft_rarity import NftRarity
from src.utils.s3_image_uploader import S3ImageUploadField
from src.views.base import MyBaseModelView

from wtforms import HiddenField


def your_namegen_func_here(file):
    return str(uuid.uuid4())


class NftDetailView(MyBaseModelView):
    column_list = ['nft_id', 'name', 'rarity_code',
                   'rarity', 'description',
                   'image', 'price', 'discount',
                   'commission',
                   'is_show', 'created_time']
    create_template = 'form/models/nft_detail/create.html'
    edit_template = 'form/models/nft_detail/edit.html'

    can_edit = True
    can_create = True
    can_delete = False
    # column_editable_list = ['price', 'is_show']
    edit_modal = False
    can_view_details = True

    form_overrides = dict(
        rarity_code=SelectField,
        image=S3ImageUploadField,
        rarity=HiddenField,
        nft_id=HiddenField,
        collection_id=SelectField,
        address=HiddenField
    )

    def image_format(view, context, model, name):
        return Markup(f'<a target="_blank" href="{model["image"]}"> image </a>')

    column_searchable_list = ['name']

    column_default_sort = ('created_time', True)

    column_formatters = {
        'image': image_format
    }

    def scaffold_form(self):
        _form = super(NftDetailView, self).scaffold_form()
        return _form

    def get_collection_options(self):
        return [(x.collection_id, x.name) for x in NftCollection.objects()]

    def get_collection_addresses(self):
        return [(x.collection_id, x.address) for x in NftCollection.objects()]

    def create_form(self, obj=None):
        self.form_widget_args = {
            'rarity': {
                'disabled': True
            }
        }

        _cols = NftDetail.objects()

        _max_id = max([col.nft_id for col in _cols]) or 0

        _form = super(NftDetailView, self).create_form(obj)

        _form.nft_id.data = _max_id + 1
        _form.collection_id.choices = self.get_collection_options()
        _form.rarity_code.choices = self.get_nft_rarity_options()

        return _form

    def edit_form(self, obj=None):
        try:

            self.form_widget_args = {
                'rarity': {
                    'disabled': True
                },
                'rarity_code': {
                    'disabled': True
                },
                'collection_id': {
                    'disabled': True
                }
            }

            self.before_is_show = obj.is_show

            self.before_price = obj.price
        except AttributeError:
            pass
        _form = super(NftDetailView, self).edit_form(obj)
        _form.rarity_code.choices = self.get_nft_rarity_options()
        _form.collection_id.choices = self.get_collection_options()

        return _form

    def get_nft_rarity_options(self):
        return [(x.code, x.name) for x in NftRarity.objects()]

    def lock_admin(self):
        return True

    def render(self, template, **kwargs):

        kwargs['factory_abi'] = factory_abi
        kwargs['factory_address'] = Config.NFT_FACTORY_ADDRESS

        kwargs['before_price'] = 0
        kwargs['before_is_show'] = False
        kwargs['address_of_collections'] = self.get_collection_addresses()
        if hasattr(self, 'before_price'):
            kwargs['before_price'] = self.before_price

        if hasattr(self, 'before_is_show'):
            kwargs['before_is_show'] = self.before_is_show

        return super(NftDetailView, self).render(template, **kwargs)
