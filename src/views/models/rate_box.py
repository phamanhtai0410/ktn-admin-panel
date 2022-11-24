from gettext import gettext

from flask import flash
from flask_admin.form import Select2Widget
from markupsafe import Markup
from pydash import find
from wtforms import HiddenField, SelectField

from src.abis import factory_abi, box_creator_abi, box_factory_abi
from src.config import Config
from src.models.box import Box
from src.models.nft_collection import NftCollection
from src.models.mesh_material import MeshMaterial
from src.models.nft_mesh import Mesh
from src.utils.s3_image_uploader import S3ImageUploadField
from src.views.base import MyBaseModelView, RowActionListMixin


class RateBoxView(MyBaseModelView, RowActionListMixin):
    column_list = ['box_id', 'mesh_index', 'mesh_material', 'proportion', 'nft_id', 'created_time']
    edit_template = 'form/models/rate_of_box/edit.html'
    create_template = 'form/models/rate_of_box/create.html'
    can_delete = False
    # can_create = False
    # edit_modal = True
    can_view_details = True

    def create_form(self, obj=None):
        _form = super(RateBoxView, self).create_form(obj)
        _boxes = Box.objects()
        _form.box_id.choices = [(x.box_id, x.name) for x in _boxes]
        print(_form.box_id.data)
        if _form.box_id.data:
            box = find(_boxes, lambda x: x.box_id == int(_form.box_id.data))
            _meshes = Mesh.objects(address=box.collection)
            _form.box_address.data = box.address
            _materials = MeshMaterial.objects(mesh_id__in=[x.mesh_id for x in _meshes])
            _form.nft_id.choices = [(x.nft_id, x.name) for x in _materials]
        return _form

    form_overrides = dict(
        box_id=SelectField,
        nft_id=SelectField,
        mesh_index=HiddenField,
        mesh_material=HiddenField,
        rarity=HiddenField,
        box_address=HiddenField
    )
    form_widget_args = {
        'address': {
            'readonly': True
        },
        'box_id': {
            'readonly': True
        }
    }

    def edit_form(self, obj=None):
        _form = super(RateBoxView, self).edit_form(obj)
        _cols = NftCollection.objects()
        _boxes = Box.objects()

        self.before_proportion = obj.proportion

        _form.box_id.choices = [(x.box_id, x.name) for x in _boxes]
        return _form

    def render(self, template, **kwargs):
        kwargs['factory_abi'] = box_factory_abi
        kwargs['factory_address'] = Config.BOX_FACTORY_ADDRESS
        kwargs['pay_token'] = Config.PAY_TOKEN
        kwargs['before_proportion'] = 0

        if hasattr(self, 'before_proportion'):
            kwargs['before_proportion'] = self.before_proportion

        return super(RateBoxView, self).render(template, **kwargs)
