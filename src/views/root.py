# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
import io
import json
import w3storage

import requests
from flask_login import login_required
from jinja2 import TemplateNotFound

from flask import Blueprint, request, render_template, redirect, url_for, jsonify
from pydash import get

from src.config import Config

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


w3 = w3storage.API(
    token=Config.IPFS_TOKEN)

def upload_file(file):
    return w3.post_upload(file)




@root_blueprint.route('/metadata_cid', methods=['POST'])
@login_required
def root_metadata():
    print(request.form.to_dict())
    _json = request.form.to_dict()
    _image = request.files['file']

    _cid = upload_file(_image)

    _metadata = {
        "description": _json['description'],
        "external_url": "",
        "image": f'https://{_cid}.ipfs.w3s.link',
        "name": _json['name'],
        'attributes': [
            {
                "trait_type": "rarity",
                "value": _json['rarity_code']
            }
        ]
    }

    print(_metadata)
    file = io.BytesIO(json.dumps(_metadata).encode())
    metadata_cid = upload_file(file)

    return jsonify({'metadata_cid': metadata_cid})
