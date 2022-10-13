from wtforms import validators

from src.views.base import MyBaseModelView


class UserView(MyBaseModelView):
    column_list = ['email', 'active', 'roles', 'is_admin']

    column_editable_list = ['active', 'is_admin']

    create_modal = True
    edit_modal = True

    form_edit_rules = ('roles', 'active', 'is_admin')

    form_create_rules = ('email', 'active', 'roles', 'password')

    form_args = {
        'roles': {
            'validators': [validators.required()]
        }
    }
