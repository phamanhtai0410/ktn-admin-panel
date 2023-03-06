# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, IntField, FloatField, BooleanField

from src.models.base import BaseDocument


class Royalty(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'royalty'
    }
    user_address = StringField(required=True)
    collection_address = StringField(required=True)
    percent = IntField(required=True, default=20, min_value=0, max_value=100)

    def __str__(self):
        return self.name if self else ''
