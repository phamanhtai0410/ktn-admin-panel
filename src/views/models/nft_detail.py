from markupsafe import Markup
from src.views.base import MyBaseModelView


class NftDetailView(MyBaseModelView):
    column_list = ['nft_id', 'name', 'type', 'rarity', 'description', 'image', 'price', 'is_show', 'created_time']
    can_edit = True
    can_create = True
    can_delete = True
    column_editable_list = ['price', 'is_show']
    edit_modal = True

    def image_format(view, context, model, name):
        # _image = model['image']
        return Markup(f'<a target="_blank" href="{model["image"]}"> image </a>')

    column_searchable_list = ['name']
    
    column_filters = ['type']

    column_default_sort = ('created_time', True)
    column_formatters = {
        'image': image_format
    }

    # def on_model_change(self, form, model, is_created):
    #     print(model)
