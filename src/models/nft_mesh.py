# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, IntField, BooleanField, FloatField, EmbeddedDocument, \
    EmbeddedDocumentField, \
    ListField, ReferenceField

from src.models.base import BaseDocument


class Mesh(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'meshes'
    }
    mesh_id = IntField(unique=True, required=True)
    name = StringField(required=True)

    collection_id = IntField()
    rarity = IntField()
    rarity_of_collection = StringField()

    mesh_index = IntField()
    price = IntField()
    address = StringField()

    description = StringField()

    image = StringField()

    discount = FloatField(min_value=0, max_value=100)
    commission = FloatField(min_value=0, max_value=100)
    commission_level_2 = FloatField(min_value=0, max_value=100)
    is_show = BooleanField(default=True)

    def __str__(self):
        return self.name if self else ''
