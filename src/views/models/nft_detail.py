from markupsafe import Markup
from wtforms import validators

from src.config import Config
from src.views.base import MyBaseModelView


class NftDetailView(MyBaseModelView):
    column_list = ['nft_id', 'name', 'rarity', 'type', 'description', 'image', 'price']
    can_edit = False
    can_create = False
    can_delete = False
    
    def image_format( view, context, model , name):
        # _image = model['image']
        return Markup(f'<a target="_blank" href="{model["image"]}"> image </a>')

    column_default_sort = ('nft_id', False)
    column_formatters = {
        'image': image_format
    }

