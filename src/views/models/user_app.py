from markupsafe import Markup
from wtforms import validators

from src.config import Config
from src.views.base import MyBaseModelView


class UserAppView(MyBaseModelView):
    column_list = ['address', 'total_points', 'total_withdraw', 'created_time']
    can_edit = False
    can_create = False
    can_delete = False

    column_labels = {
        'address': 'User',
        'created_time': 'Joint at'
    }

    def address_formart(view, context, model, name):
        _address = model['address']
        return Markup(f'<a target="_blank"  href="{Config.BSC_SCAN}/address/{_address}">{_address}</a>')

    column_searchable_list = ['address']

    column_default_sort = ('created_time', True)

    column_formatters = {
        'address': address_formart
    }
