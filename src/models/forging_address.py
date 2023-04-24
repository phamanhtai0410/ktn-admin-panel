# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, ListField

from src.models.base import BaseDocument


class ForgingAddress(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'forging_address'
    }
    chain = StringField(choices=["BSC", "AVAX", "POLYGON", "BOBA"], required=True)
    collection_type = StringField(choices=["2D", "3D"], required=True)
    collection_address = ListField(StringField(), required=True)

