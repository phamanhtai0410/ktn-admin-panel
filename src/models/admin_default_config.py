# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField
from src.models.base import BaseDocument


class AdminDefaultConfigs(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'admin_default_configs'
    }
    type = StringField(required=True)
    name = StringField(required=True)
    value = StringField(required=True)

