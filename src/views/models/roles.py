from wtforms import validators
from flask import request, Markup
from flask_admin import form
import bson

from src.models.security import User
from src.routes import ROLES__PAGE_ACCESS_DISPLAY
from src.setting.default_formatter import DEFAULT_TYPE_FORMATTER
from src.views.base import MyBaseModelView

class RolesView(MyBaseModelView):

    def access_formart(view, context, model, name):
        permission = ''
        for access in model['access']:
            action = ['<b>' + i + '</b>' for i in access['action']
                      if access['action'][i] == True]
            action = ', '.join(action) if len(action) > 0 else '<b>view</b>'
            permission += f'<p>• {ROLES__PAGE_ACCESS_DISPLAY[access["page"]]}: {action}</p>'
        return Markup(permission)

    create_modal = True
    edit_modal = True

    column_formatters = {
        'access': access_formart
    }

    column_type_formatters = DEFAULT_TYPE_FORMATTER

    column_list = ['name', 'description',
                   'access', 'updated_time', 'updated_by']

    # create_modal = True
    # edit_modal = True

    column_default_sort = ('updated_time', True)

    form_choices = {
        'access.page': ()
    }

    form_args = {
        'name': {
            'validators': [validators.required()]
        },
        'access.action': {
            "widget": form.Select2Widget(),
            'render_kw': {"multiple": "multiple"}
        },
    }

    def on_model_delete(self, model):
        role_id = model['id']

        # remove roles deleted of users
        User.update_by_query(
            query={
                'roles': bson.ObjectId(role_id)
            },
            data={
                "pull__roles": bson.ObjectId(role_id)
            }
        )
        pass
