# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, IntField, ListField, DictField, BooleanField, FloatField
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
    total_supply = IntField(required=True,default=10000, min_value=1)
    # delist = BooleanField(default=False)
    disable_mint = BooleanField(default=False)
    royalty_rate = FloatField(required=True, default=20, min_value=0, max_value=100)

    def __str__(self):
        return self.name if self else ''
