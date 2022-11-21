import io
import json
import uuid
from gettext import gettext

import requests
from flask import request, flash
from flask_admin.form import RenderTemplateWidget
from wtforms.fields.core import SelectField

from src.abis import factory_abi
from src.config import Config
from src.models.mesh_material import MeshMaterial
from src.models.nft_mesh import Mesh
from src.models.nft_rarity import NftRarity
from src.utils.s3_image_uploader import S3ImageUploadField
from src.views.base import MyBaseModelView

from wtforms import HiddenField, validators


def your_namegen_func_here(file):
    return str(uuid.uuid4())


class MeshMaterialView(MyBaseModelView):
    column_list = ['name', 'mesh_index', 'material', 'cid', 'created_time']

    create_template = 'form/models/mesh_material/create.html'
    # edit_template = 'form/models/nft_detail/edit.html'

    can_edit = True
    can_create = True
    can_delete = False

    can_view_details = True

    form_overrides = dict(
        mesh_id=SelectField,
        image=S3ImageUploadField,
        cid=HiddenField,
        mesh_index=HiddenField,
        nft_id=HiddenField
    )

    column_searchable_list = []

    column_default_sort = ('nft_id', True)

    def create_form(self, obj=None):
        self.form_widget_args = {

        }

        _form = super(MeshMaterialView, self).create_form(obj)
        _form.mesh_id.choices = self.get_mesh_options()
        _cols = MeshMaterial.objects()
        _max_id = 0

        if _cols:
            _max_id = max([col.nft_id for col in _cols]) or 0

        _form.nft_id.data = _max_id + 1

        return _form

    def edit_form(self, obj=None):
        try:

            self.form_widget_args = {
                'nft_id': {
                    'readonly': True,
                },
                'mesh_index': {
                    'readonly': True
                },
                'material': {
                    'readonly': True
                },
                'mesh_id': {
                    'readonly': True
                },
                'image': {
                    'disabled': True
                }
            }

        except AttributeError:
            pass
        _form = super(MeshMaterialView, self).edit_form(obj)
        _form.mesh_id.choices = self.get_mesh_options()
        return _form

    def get_mesh_options(self, collection=None):
        return [(f'{x.mesh_id}', x.name) for x in Mesh.objects()]

    def render(self, template, **kwargs):

        kwargs['factory_abi'] = factory_abi
        kwargs['factory_address'] = Config.NFT_FACTORY_ADDRESS

        kwargs['before_price'] = 0
        kwargs['before_is_show'] = False
        kwargs['address_of_collections'] = []
        if hasattr(self, 'before_price'):
            kwargs['before_price'] = self.before_price

        if hasattr(self, 'before_is_show'):
            kwargs['before_is_show'] = self.before_is_show

        return super(MeshMaterialView, self).render(template, **kwargs)

    def create_model(self, *args, **kwargs):
        try:
            return super(MeshMaterialView, self).create_model(*args, **kwargs)
        except Exception as e:
            flash(gettext(str(e)), 'error')
