from flask_admin.form import Select2Widget
from markupsafe import Markup
from mongoengine.base import BaseList
from wtforms import validators, SelectMultipleField
from wtforms.fields.core import UnboundField

from src.models.nft_detail import NftDetail
from src.views.base import MyBaseModelView, RowActionListMixin
from src.utils.s3_image_uploader import S3ImageUploadField

from wtforms.fields import SelectMultipleField


def get_nfts_options():
    return [(f'{x.nft_id}', x.name) for x in NftDetail.objects()]


class NftCollectionView(MyBaseModelView, RowActionListMixin):
    column_list = ['collection_id', 'name', 'description', 'image', 'nfts', 'created_time']
    create_modal = True
    edit_modal = True
    column_labels = {
        'collection_id': 'Id'
    }
    form_overrides = dict(
        nfts=SelectMultipleField,
        image=S3ImageUploadField
    )

    form_args = {}

    def image_format(view, context, model, name):
        # _image = model['image']
        return Markup(f'<a target="_blank" href="{model["image"]}"> image </a>')

    def nfts_format(view, context, model, name):
        # print([x.id for x in view.get_nfts()])
        _nfts = [(x.name, x.id) for x in view.get_nfts() if x.nft_id in model['nfts']]
        if not _nfts:
            return ""
        permission = '<ul>'
        for item in _nfts:
            permission += f'<li> <a href="/nftdetail/details/?id={item[1]}"> {item[0]}</a></li>'
        return Markup(permission + "</ul>")

    def scaffold_form(self):
        self.form_args = {
            'nfts': {
                'choices': [],
                'widget': Select2Widget(multiple=True)
            }
        }
        return super(NftCollectionView, self).scaffold_form()

    def get_nfts(self):
        return NftDetail.objects()

    def create_form(self, obj=None):
        _form = super(NftCollectionView, self).create_form(obj)
        _form.nfts.choices = get_nfts_options()
        return _form

    def edit_form(self, obj=None):
        _form = super(NftCollectionView, self).edit_form(obj)
        _form.nfts.choices = self.get_nfts_options()
        return _form

    def get_nfts_options(self):
        return [(f'{x.nft_id}', x.name) for x in NftDetail.objects()]

    column_searchable_list = ['name']

    column_default_sort = ('created_time', True)
    column_formatters = {
        'image': image_format,
        'nfts': nfts_format
    }
