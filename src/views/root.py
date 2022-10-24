# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from flask_login import login_required
from jinja2 import TemplateNotFound

from flask import Blueprint, request, render_template, redirect, url_for, jsonify

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

# @root_blueprint.route('/get_nft_detail', methods= ['POST'])
# @login_required
# def index():
#     nfts= {
#         'nft_id': 1,
#         'name': 'thanh',
#         'rarity': 2,
#         'is_active': True
#     }
#     print(nfts)
#     return jsonify({'htmlresponse': render_template('custom/nft_type.html',nfts=nfts)})
    # return nfts
    # return redirect(url_for('admin.index'))