# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, IntField, FloatField

from src.models.base import BaseDocument


class EmailSubscribe(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'email_subscribe'
    }
    email = StringField()
