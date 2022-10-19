from flask_admin.model.template import DeleteRowAction, EditRowAction
from src.views.base import MyBaseModelView, RowActionListMixin


class PromotionView(RowActionListMixin, MyBaseModelView):
    column_list = ['code', 'discount', 'status', 'created_time', 'updated_time', 'updated_by']
    can_edit = True
    can_create = True
    can_delete = True

    column_searchable_list = ['code']

    column_default_sort = ('created_time', True)

    def _can_edit(self, model):
        # Put your logic here to allow edit per model
        # return True to allow edit
        return model.status

    def _can_delete(self, model):
        # Put your logic here to allow delete per model
        # return True to allow delete
        return model.status

    def allow_row_action(self, action, model):

        # # Deal with Edit Action
        if isinstance(action, EditRowAction):
            return self._can_edit(model)

        # # Deal with Delete Action
        if isinstance(action, DeleteRowAction):
            return self._can_delete(model)

        # # Deal with other actions etc

        # otherwise whatever the inherited method returns
        return super().allow_row_action()
