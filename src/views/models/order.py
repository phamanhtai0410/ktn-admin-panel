from markupsafe import Markup
from wtforms import validators

from src.views.base import MyBaseModelView


class OrderView(MyBaseModelView):
    column_list = ['order_id', 'address', 'items', 'status', 'created_time']
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
        return Markup(permission+"</ul>")

    column_searchable_list = ['address', 'order_id']

    column_default_sort = ('created_time', True)

    column_formatters = {
        'items': items_formart
    }
