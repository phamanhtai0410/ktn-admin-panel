# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
import io
import json
import traceback
from datetime import datetime

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


def upload_files(files):
    return w3.post_upload(files)


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
                "value": _json['rarity']
            },
            {
                "trait_type": "mesh_index",
                "value": _json['mesh_index']
            },
            {
                "trait_type": "mesh_material",
                "value": _json['material']
            }
        ]
    }

    print(_metadata)
    file = io.BytesIO(json.dumps(_metadata).encode())
    metadata_cid = upload_file(file)
    print('metadata_cid', metadata_cid)
    return jsonify({'metadata_cid': metadata_cid})


@root_blueprint.route('/box_cid', methods=['POST'])
@login_required
def box_cid():
    print(request.form.to_dict())
    _json = request.form.to_dict()
    _image = request.files['file']

    _cid = upload_file(_image)

    _metadata = {
        "description": _json['description'],
        "external_url": "",
        "image": f'https://{_cid}.ipfs.w3s.link',
        "name": _json['name'],
        'attributes': []
    }

    print(_metadata)
    file = io.BytesIO(json.dumps(_metadata).encode())
    metadata_cid = upload_file(file)
    print('metadata_cid', metadata_cid)
    return jsonify({'metadata_cid': metadata_cid})


@root_blueprint.route('/file/ipfs', methods=['POST'])
def upload_ipfs():
    _file = request.files['file']
    file = io.BytesIO(f'Game upload at: {datetime.now()}'.encode())

    _cid = upload_files(_file)
    return jsonify({'ipfs': f'https://{_cid}.ipfs.w3s.link'})

#
# @root_blueprint.route('/prices', methods=['GET'])
# def get_prices():
#     try:
#         res = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=binancecoin,tether,wbnb")
#         print(res.json())
#         return jsonify(res.json())
#     except:
#         traceback.print_exc()
#     return jsonify({})
