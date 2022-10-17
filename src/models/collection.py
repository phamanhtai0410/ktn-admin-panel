# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, IntField

from src.models.base import BaseDocument


class Collection(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'collection'
    }
    collection_id = IntField()
    name = StringField()
    description = StringField()
    image = StringField()

    def __str__(self):
        return self.collection_id if self else ''

