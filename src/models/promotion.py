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
    code = StringField()
    discount = FloatField()
    status = BooleanField()
