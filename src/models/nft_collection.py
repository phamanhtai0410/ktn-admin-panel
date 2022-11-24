# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, IntField, ListField, DictField, BooleanField
from src.models.base import BaseDocument


class NftCollection(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'collection'
    }
    collection_id = IntField(required=True, unique=True)
    name = StringField(required=True)
    symbol = StringField(required=True)
    description = StringField(required=True)
    image = StringField(required=True)
    address = StringField()
    max_rarity = IntField(default=0)
    block_number = IntField()
    delist = BooleanField(default=False)

    def __str__(self):
        return self.name if self else ''
