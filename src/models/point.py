# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, IntField, FloatField

from src.models.base import BaseDocument


class PointLog(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'point_logs'
    }
    address = StringField()
    amount = FloatField()
    action = StringField()
    ref_id = StringField()

    def __str__(self):
        return self.ref_id if self else ''
