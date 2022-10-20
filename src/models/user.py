# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, FloatField

from src.models.base import BaseDocument


class UserApp(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'user'
    }
    address = StringField()
    total_points = FloatField()
    total_withdraw = FloatField()

    def __str__(self):
        return self.address if self else ''
