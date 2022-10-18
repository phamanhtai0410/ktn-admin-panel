# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField

from src.models.base import BaseDocument


class UserApp(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'user'
    }
    address = StringField()

    def __str__(self):
        return self.address if self else ''
