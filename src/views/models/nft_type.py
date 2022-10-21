from markupsafe import Markup
from src.views.base import MyBaseModelView


class NftTypeView(MyBaseModelView):
    column_list = ['collection_id', 'name', 'description', 'image', 'created_time']
    create_modal = True
    edit_modal = True
    
    column_labels = {
        'collection_id': 'Nft Type'
    }
    
    def image_format( view, context, model , name):
        # _image = model['image']
        return Markup(f'<a target="_blank" href="{model["image"]}"> image </a>')

    def items_format( view, context, model , name):
        # _image = model['image']
        return Markup(f'<a target="_blank" href="admin/model/modals/create.html"> items </a>')
    
    column_searchable_list = ['name']

    column_default_sort = ('created_time', True)
    column_formatters = {
        'image': image_format,
    }

