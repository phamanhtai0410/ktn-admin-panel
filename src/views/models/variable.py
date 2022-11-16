from markupsafe import Markup
from wtforms import SelectField
from wtforms.widgets import html_params, HTMLString

from src.models.nft_detail import NftDetail
from src.utils.s3_image_uploader import S3ImageUploadField
from src.views.base import MyBaseModelView



class VariableView(MyBaseModelView):
    column_list = ['type_id', 'nft_id', 'rarity_id', 'image', 'price', 'created_time']
    can_edit = True
    can_create = True
    can_delete = True
    form_overrides = dict(
        image=S3ImageUploadField,
        nft_id=SelectField
    )

    column_default_sort = ('nft_id', True)

    def image_format(view, context, model, name):
        return Markup(f'<a target="_blank" href="{model["image"]}"> logo </a>')

    column_formatters = {
        'image': image_format

    }

    def create_form(self, obj=None):
        _form = super(VariableView, self).create_form(obj=obj)
        _form.nft_id.choices = [(x.nft_id, f'{x.nft_id}:{x.name} - {x.rarity_code}') for x in NftDetail.objects()]
        return _form

