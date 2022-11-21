import io
import json
import traceback
import uuid

import requests
from flask import request, jsonify, url_for
from flask_admin import expose
from flask_admin.form import RenderTemplateWidget
from flask_admin.model.fields import InlineFieldList
from flask_admin.model.widgets import InlineFieldListWidget
from markupsafe import Markup
from pydash import get
from wtforms.fields.core import SelectField

from src.abis import factory_abi
from src.config import Config
from src.models.mesh_material import MeshMaterial
from src.models.nft_collection import NftCollection
from src.models.nft_mesh import Mesh
from src.models.nft_rarity import NftRarity
from src.utils.s3_image_uploader import S3ImageUploadField
from src.views.base import MyBaseModelView

from wtforms import HiddenField, SelectField


def your_namegen_func_here(file):
    return str(uuid.uuid4())


class TypesFieldListWidget(RenderTemplateWidget):
    def __init__(self):
        super(TypesFieldListWidget, self).__init__('widgets/nft_types.html')


class CustomSelectDependWidget(SelectField):
    def __init__(self, field_depend, *args, **kwargs):
        self.field_depend = field_depend
        super(CustomSelectDependWidget, self).__init__(*args, **kwargs)

    def __call__(self, **kwargs):
        kwargs.setdefault('data-depend', self.field_depend)
        # Or call select2 in tags mode

        return super(CustomSelectDependWidget, self).__call__(**kwargs)


class MeshView(MyBaseModelView):
    column_list = ['mesh_id',
                   'mesh_index',
                   'name',
                   'rarity',
                   'description',
                   'price',
                   'variables',
                   'discount',
                   'commission',
                   'is_show', 'created_time']

    def on_model_change(self, form, model, is_created):
        try:
            if is_created:
                _rarity_of_collection = form.rarity_of_collection.data.split("_")
                model.rarity = int(_rarity_of_collection[0])
                model.collection_id = int(_rarity_of_collection[1])
                model.address = _rarity_of_collection[2]

        except:
            traceback.print_exc()

    # create_template = 'form/models/mesh/create.html'
    edit_template = 'form/models/mesh/edit.html'

    can_edit = True
    can_create = True
    can_delete = False
    edit_modal = False
    can_view_details = True

    form_overrides = dict(
        image=S3ImageUploadField,
        rarity=HiddenField,
        mesh_id=HiddenField,
        collection_id=HiddenField,
        address=HiddenField,
        rarity_of_collection=SelectField
    )

    def image_format(view, context, model, name):
        return Markup(f'<a target="_blank" href="{model["image"]}"> image </a>')

    def variables_format(self, context, model, name):
        _variables = MeshMaterial.objects(mesh_id=model['mesh_id'])
        permission = '<ul>'
        for item in _variables:
            permission += f'<li href="{item.image}" target="_blank" >{item.type_id}: {item.price} USD </li>'
        permission += f'<li ><a href="{url_for("meshmaterial.create_view", mesh_id=model["mesh_id"])}"><i class="fa fa-plus-circle" aria-hidden="true"></i></a></li>'
        return Markup(permission + "</ul>")

    column_searchable_list = ['name']

    column_default_sort = ('created_time', True)

    column_formatters = {
        'image': image_format,
        'variables': variables_format
    }

    def scaffold_form(self):
        _form = super(MeshView, self).scaffold_form()
        return _form

    def get_rarity_of_collection_options(self):
        return [(f'{x.rarity_id}_{x.collection_id}_{x.collection_address}', f'{x.name} - {x.collection_address}') for x
                in NftRarity.objects()]

    def create_form(self, obj=None):
        self.form_widget_args = {
            'rarity': {
                'readonly': True
            }
        }

        _cols = Mesh.objects()
        _max_id = 0
        if _cols:
            _max_id = max([col.mesh_id for col in _cols]) or 0

        _form = super(MeshView, self).create_form(obj)

        _form.mesh_id.data = _max_id + 1
        _form.rarity_of_collection.choices = self.get_rarity_of_collection_options()

        return _form

    def edit_form(self, obj=None):
        try:

            self.form_widget_args = {
                'rarity': {
                    'readonly': True
                },
                'rarity_of_collection': {
                    'readonly': True
                },
                'collection_id': {
                    'readonly': True
                }
            }

            self.before_is_show = obj.is_show

            self.before_price = obj.price
        except AttributeError:
            pass
        _form = super(MeshView, self).edit_form(obj)
        _form.rarity_of_collection.choices = self.get_rarity_of_collection_options()

        return _form

    def lock_admin(self):
        return True

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

        return super(MeshView, self).render(template, **kwargs)

    @expose('/mesh', methods=['POST'])
    def get_mesh(self):
        _data = request.json

        print('get_mesh', _data)

        _mesh = Mesh.objects(mesh_id=_data['mesh_id']).first()
        if not _mesh:
            raise Exception
        print("_____________")

        return jsonify({
            'mesh_id': _mesh.mesh_id,
            'price': str(_mesh.price),
            'address': _mesh.address,
            'rarity': _mesh.rarity,
            'mesh_index': _mesh.mesh_index,
            'name': _mesh.name
        })
