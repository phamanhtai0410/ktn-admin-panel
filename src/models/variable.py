# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, IntField, FloatField

from src.models.base import BaseDocument


class Variable(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'variables'
    }
    nft_id = IntField(required=True)
    type_id = IntField(unique_with='nft_id')
    image = StringField(required=True)
    price = FloatField(required=True)

    def __str__(self):
        return self.type_id if self else ''
