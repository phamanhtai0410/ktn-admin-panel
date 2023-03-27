from src.views.base import MyBaseModelView, RowActionListMixin
from flask import flash, request, url_for
from gettext import gettext


class AdminDefaultConfigsView(MyBaseModelView, RowActionListMixin):
    # View column
    column_list = [
        'type',
        'name',
        'value'
    ]
    
    can_delete = False

    def create_form(self, obj=None):
        _form = super(AdminDefaultConfigsView, self).create_form(obj)
        return _form
    
    def edit_form(self, obj=None):
        self.form_widget_args = {
            'type': {
                'readonly': True
            },
            'name': {
                'readonly': True
            }
        }
        _form = super(AdminDefaultConfigsView, self).edit_form(obj)
        return _form
    
    column_searchable_list = ['name']
    column_default_sort = ('created_time', True)

    def render(self, template, **kwargs):
        return super(AdminDefaultConfigsView, self).render(template, **kwargs)
    
    def create_model(self, form):
        try:
            return super(AdminDefaultConfigsView, self).create_model(form)
        except Exception as e:
            flash(gettext(str(e)), 'error')