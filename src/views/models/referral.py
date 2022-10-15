from src.views.base import MyBaseModelView


class ReferralView(MyBaseModelView):
    column_list = ['address', 'code', 'address_linked', 'code_linked', 'created_time']
    can_edit = False
    can_create = False
    can_delete = False

    column_searchable_list = ['address', 'address_linked', 'code', 'code_linked']

    column_default_sort = ('created_time', True)
