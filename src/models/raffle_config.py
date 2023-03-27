# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, IntField
from src.models.base import BaseDocument


class RaffleConfig(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'raffle_config'
    }
    name = StringField(required=True)
    start_time = IntField(required=True)
    end_time = IntField(required=True)
    point_per_task = IntField(required=True)

