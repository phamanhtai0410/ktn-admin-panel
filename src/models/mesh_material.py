# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, IntField, FloatField, BooleanField

from src.models.base import BaseDocument


class MeshMaterial(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'mesh_materials'
    }
    name = StringField(required=True)
    nft_id = IntField()
    mesh_id = IntField(required=True)
    mesh_index = IntField()
    material = IntField(required=True)
    image = StringField(required=True)
    description = StringField(required=True)

    cid = StringField()
    is_show = BooleanField(default=True)

    def __str__(self):
        return self.name if self else ''
