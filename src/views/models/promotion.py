import random
import string

from flask import request, redirect
from flask_admin import expose
from flask_admin.model.template import DeleteRowAction, EditRowAction

from src.models.promotion import Promotion
from src.views.base import MyBaseModelView, RowActionListMixin


class PromotionView(RowActionListMixin, MyBaseModelView):
    column_list = ['code', 'discount', 'used', 'total', 'created_time', 'updated_time', 'updated_by']
    can_edit = True
    can_create = True
    can_delete = True

    column_searchable_list = ['code']

    list_template = 'custom/menu_bar.html'

    column_default_sort = ('created_time', True)

    @expose('/create_multi', methods=['POST'])
    def create_multi(self):
        quantity = int(request.form['quantity'])
        discount = int(request.form['discount'])
        length = 8

        for i in range(quantity):
            letters = string.ascii_uppercase + string.digits
            code = ''.join(random.choice(letters) for i in range(length))
            Promotion(code=code, discount=discount, status=True).save()

        return redirect('/promotion/')

    def _can_edit(self, model):
        
        # Put your logic here to allow edit per model
        # return True to allow edit
        return not (model.used >= model.total)

    def _can_delete(self, model):
        # Put your logic here to allow delete per model
        # return True to allow delete
        return not (model.used >= model.total)

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
