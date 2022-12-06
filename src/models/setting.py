# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, IntField

from src.models.base import BaseDocument


class Setting(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'setting'
    }
    referral_cookies = IntField()
