# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, IntField, ObjectIdField, BooleanField

from src.models.base import BaseDocument


class Payment(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'payment'
    }
    _id = ObjectIdField()
    asset = StringField()
    chain = StringField()
    chain_id = IntField()
    asset_logo = StringField()
    chain_logo = StringField()
    is_active = BooleanField()

    def __str__(self):
        return self.collection_id if self else ''

