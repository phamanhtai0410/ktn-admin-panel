from markupsafe import Markup
from src.views.base import MyBaseModelView


class CollectionView(MyBaseModelView):
    column_list = ['collection_id', 'name', 'description', 'image', 'created_time']
    can_edit = True
    can_create = True
    can_delete = True
    
    def image_format( view, context, model , name):
        # _image = model['image']
        return Markup(f'<a target="_blank" href="{model["image"]}"> image </a>')

    column_searchable_list = ['name']

    column_default_sort = ('collection_id', False)
    column_formatters = {
        'image': image_format
    }

