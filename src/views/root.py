# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from flask_login import login_required
from jinja2 import TemplateNotFound

from flask import Blueprint, request, render_template, redirect, url_for

root_blueprint = Blueprint(
    'root_blueprint',
    __name__,
    url_prefix=''
)


# Helper - Extract current page name from request
def get_segment(request):
    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None


@root_blueprint.route('/')
@login_required
def root_view():
    return redirect(url_for('admin.index'))
