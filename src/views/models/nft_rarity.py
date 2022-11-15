from markupsafe import Markup
from pydash import get, slugify

from src.connect import bsc
from src.views.base import MyBaseModelView, RowActionListMixin
from flask_admin import expose
from flask import request, redirect, render_template

from wtforms import validators


class NftRarityView(MyBaseModelView, RowActionListMixin):
    column_list = ['name', 'code', 'created_time']
    create_modal = True
    edit_modal = True
    # list_template = 'custom/nft_type.html'
    can_delete = False

    form_widget_args = {
        'code': {
            'disabled': True
        }
    }

    column_searchable_list = ['name']

    column_default_sort = ('created_time', True)

    def on_model_change(self, form, model, is_created):

        try:

            if is_created and not model.code:
                model.code = slugify(model.name).upper()

        except Exception as e:
            raise validators.ValidationError(e)

