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
from wtforms.fields.core import SelectField, BooleanField, StringField

from src.abis import factory_abi, royalty_controller_abi
from src.config import Config
from src.models.mesh_material import MeshMaterial
from src.models.nft_collection import NftCollection
from src.models.nft_mesh import Mesh
from src.models.nft_rarity import NftRarity
from src.utils.s3_image_uploader import S3ImageUploadField
from src.views.base import MyBaseModelView

from wtforms import HiddenField, SelectField, Form

from wtforms.validators import DataRequired



class RoyaltyConfigView(MyBaseModelView):
    column_list = ['user_address',
                   'collection_address',
                   'percent', 'created_time']
    can_edit = False
    can_delete = False
    #
    # def on_model_change(self, form, model, is_created):
    #     try:
    #         if is_created:
    #             model.collection_address = NftCollection.objects(collection_id=form.collection_id.data).first().address
    #
    #     except:
    #         traceback.print_exc()

    create_template = 'form/models/royalty/create.html'
    # cewe = 'form/models/mesh/edit.html'

    can_view_details = True
    # form = GreetingsForm
    
    form_overrides = dict(
        # collection_id=SelectField,
        collection_address=SelectField,
    )

    def image_format(view, context, model, name):
        return Markup(f'<a target="_blank" href="{model["image"]}"> image </a>')

    def get_collections(self):
        return [(x.address, x.address) for x in NftCollection.objects()]

    column_default_sort = ('created_time', True)

    column_formatters = {
    }

    def create_form(self, obj=None):
        self.form_widget_args = {}

        _cols = Mesh.objects()
        _form = super(RoyaltyConfigView, self).create_form(obj)
        _form.collection_address.choices = self.get_collections()
        
        return _form

    def lock_admin(self):
        return True

    def render(self, template, **kwargs):

        kwargs['abi'] = royalty_controller_abi
        kwargs['controller_address'] = Config.ROYALTY_CONTROLLER_ADDRESS 

        return super(RoyaltyConfigView, self).render(template, **kwargs)
