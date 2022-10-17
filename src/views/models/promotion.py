from flask_admin.model.template import DeleteRowAction, EditRowAction

from src.views.base import MyBaseModelView


class PromotionView(MyBaseModelView):
    column_list = ['address', 'code', 'discount', 'status', 'created_time', 'updated_time', 'updated_by']
    can_edit = True
    can_create = True
    can_delete = True

    column_labels = {
        'address': 'User'
    }

    column_searchable_list = ['address', 'code']

    column_default_sort = ('created_time', True)
