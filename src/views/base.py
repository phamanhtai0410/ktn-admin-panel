# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from flask import redirect, url_for, request, flash, session
from flask_admin import AdminIndexView, BaseView
from flask_admin.contrib.mongoengine import ModelView
from flask_login import current_user, logout_user

from src.routes import LOCK_PAGE


class MyBaseModelView(ModelView):
    def is_accessible(self):
        # if user is inactive when using, logout this user
        if not current_user.is_authenticated or current_user['active'] == False:
            session.clear()
            logout_user()
            return current_user.is_authenticated
        is_render_page = False

        # SHOW ALL FOR SUPPER ADMIN
        if current_user.is_admin:
            is_render_page = True
            print(self.name)
            if self.name not in LOCK_PAGE:
                self.edit = True
                self.can_create = True
                self.can_delete = True
                self.can_export = True
        else:
            if current_user.roles:
                for role in current_user.roles:
                    for access in role.access:
                        if access.page in self.endpoint:
                            is_render_page = True
                            self.can_edit = access.action['edit']
                            self.can_create = access.action['create']
                            self.can_delete = access.action['delete']
                            self.can_export = access.action['export']
                            self.view_details = access.action['view_details']

        return current_user.is_authenticated and is_render_page

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        if current_user.is_authenticated:
            flash('You do not have permission')
            return redirect(url_for('admin.index', next=request.url))
        return redirect(url_for('security.login', next=request.url))

    # create_template = 'admin/base/create.html'
    form_excluded_columns = [
        'created_time', 'created_by',
        'updated_time', 'updated_by',
    ]


class MyBaseModelViewUX(BaseView):
    def is_accessible(self):
        # print(current_user)
        # print(current_user.is_authenticated)
        # if user is inactive when using, logout this user
        if not current_user.is_authenticated or current_user['active'] == False:
            session.clear()
            logout_user()
            return current_user.is_authenticated
        is_render_page = False
        # if user is admin - always have role and user permission
        if current_user.is_admin:
            is_render_page = True
            self.edit = True
            self.can_create = True
            self.can_delete = True
            self.can_export = True
        else:
            if current_user.roles:
                for role in current_user.roles:
                    for access in role.access:
                        if access.page in self.endpoint:
                            is_render_page = True
                            self.can_edit = access.action['edit']
                            self.can_create = access.action['create']
                            self.can_delete = access.action['delete']
                            self.can_export = access.action['export']
                            self.view_details = access.action['view_details']

        return current_user.is_authenticated and is_render_page

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        if current_user.is_authenticated:
            flash('You do not have permission')
            return redirect(url_for('admin.index', next=request.url))
        return redirect(url_for('security.login', next=request.url))


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('security.login', next=request.url))


class RowActionListMixin(object):
    list_template = 'admin/list.html'

    def allow_row_action(self, action, model):
        return True
