from markupsafe import Markup
from wtforms import validators

from src.views.base import MyBaseModelView


class NftView(MyBaseModelView):
    column_list = ['token_id', 'address', 'rarity', 'created_time']
    can_edit = False
    can_create = False
    can_delete = False

    column_labels = {
        'address': 'User'
    }

    column_searchable_list = ['address', 'token_id']

    column_default_sort = ('created_time', True)
