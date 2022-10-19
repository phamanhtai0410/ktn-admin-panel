# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, BooleanField, FloatField

from src.models.base import BaseDocument


class Promotion(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'promotion_codes'
    }
    address = StringField(required=False)
    code = StringField(required=True, unique=True)
    discount = FloatField(required=True)
    status = BooleanField(default=True)
