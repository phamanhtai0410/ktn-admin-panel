from markupsafe import Markup
from wtforms import validators

from src.config import Config
from src.views.base import MyBaseModelView


class OrderView(MyBaseModelView):
    column_list = ['order_id', 'address', 'items', 'status', 'tx_hash', 'created_time']
    can_edit = False
    can_create = False
    can_delete = False

    column_labels = {
        'address': 'User'
    }

    def items_formart(view, context, model, name):
        permission = '<ul>'
        for item in model['items']:
            permission += f'<li>{item.name}: {item.amount} - {item.price} USD/item </li>'
        return Markup(permission + "</ul>")

    def address_formart(view, context, model, name):
        _address = model['address']
        return Markup(f'<a target="_blank"  href="{Config.BSC_SCAN}/address/{_address}">{_address}</a>')

    def tx_hash_formart(view, context, model, name):
        _tx_hash = model.tx_hash
        if isinstance(_tx_hash, str) and len(_tx_hash) > 12:
            return Markup(
                f'<a target="_blank"  href="{Config.BSC_SCAN}/tx/{_tx_hash}">{_tx_hash[:4]}...{_tx_hash[-4:]}</a>')
        return Markup("<p style='color: #808080;'>WAITING</p>")

    def status_formart(view, context, model, name):
        _status = model.status
        if _status in ['FAILED', 'ERROR']:
            return Markup(
                f'<ul ><li>{_status}</li><li>{model.reason}</li></ul>')
        return _status

    column_searchable_list = ['address', 'order_id']

    column_default_sort = ('created_time', True)

    column_formatters = {
        'items': items_formart,
        'address': address_formart,
        'tx_hash': tx_hash_formart,
        'status': status_formart
    }
