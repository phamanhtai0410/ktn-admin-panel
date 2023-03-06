# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, BooleanField, FloatField, IntField

from src.models.base import BaseDocument


class Promotion(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'promotion_codes'
    }
    code = StringField(required=True, unique=True)
    discount = FloatField(required=True, default=0.04)
    used = IntField(required=True)
    total = IntField(required=True)
