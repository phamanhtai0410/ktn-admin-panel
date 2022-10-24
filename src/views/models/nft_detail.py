from markupsafe import Markup
from src.views.base import MyBaseModelView


class NftDetailView(MyBaseModelView):
    column_list = ['nft_id', 'name', 'rarity', 'type', 'description', 'image', 'price','is_show', 'created_time']
    can_edit = True
    can_create = True
    can_delete = True
    
    def image_format( view, context, model , name):
        # _image = model['image']
        return Markup(f'<a target="_blank" href="{model["image"]}"> image </a>')

    column_searchable_list = ['name']

    column_default_sort = ('created_time', True)
    column_formatters = {
        'image': image_format
    }

