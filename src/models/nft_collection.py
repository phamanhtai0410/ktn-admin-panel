# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, IntField, ListField, DictField
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
    # nfts = ListField(IntField(), default=[])
    # rarity_nfts = ListField(DictField())
    address = StringField()
    max_rarity = IntField(default=0)

    def __str__(self):
        return self.name if self else ''
