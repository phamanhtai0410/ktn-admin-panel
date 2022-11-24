# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, BooleanField, ListField, EmbeddedDocument, IntField, FloatField, \
    EmbeddedDocumentField

from src.models.base import BaseDocument


class RateOfBox(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'rate_of_boxes'
    }
    rarity = IntField()
    mesh_index = IntField()
    mesh_material = IntField()
    nft_id = IntField()
    box_id = IntField()
    proportion = IntField(min_value=0, max_value=100)
    box_address = StringField()
    
    def __str__(self):
        return f'{self.nft_id}: {self.proportion}' if self else ''
