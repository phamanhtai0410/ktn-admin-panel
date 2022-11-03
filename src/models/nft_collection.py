# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, IntField, ListField

from src.models.base import BaseDocument


class NftCollection(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'collection'
    }
    collection_id = IntField()
    name = StringField()
    description = StringField()
    image = StringField()
    nfts = ListField(IntField(), default=[])

    def __str__(self):
        return self.name if self else ''

