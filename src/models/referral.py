# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField

from src.models.base import BaseDocument


class Referral(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'referral'
    }
    address = StringField()
    address_linked = StringField()
    code = StringField()
    code_linked = StringField()
