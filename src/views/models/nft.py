from markupsafe import Markup
from wtforms import validators

from src.config import Config
from src.views.base import MyBaseModelView


class NftView(MyBaseModelView):
    column_list = ['token_id', 'address', 'rarity', 'created_time']
    can_edit = False
    can_create = False
    can_delete = False

    column_labels = {
        'address': 'User'
    }

    def address_formart(view, context, model, name):
        _address = model['address']
        return Markup(f'<a target="_blank"  href="{Config.BSC_SCAN}/address/{_address}">{_address}</a>')

    def token_formart(view, context, model, name):
        _contract = model['contract']
        return Markup(f'<a target="_blank"  href="{Config.BSC_SCAN}/address/{_contract}">{model["token_id"]}</a>')

    column_searchable_list = ['address', 'token_id']

    column_default_sort = ('created_time', True)

    column_formatters = {
        'address': address_formart,
        'token_id': token_formart
    }
