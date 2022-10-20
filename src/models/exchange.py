# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, IntField, FloatField

from src.models.base import BaseDocument


class ExchangeLog(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'exchange_logs'
    }
    address = StringField()
    dev_account = StringField()
    tx_hash = StringField()
    amount = FloatField()
    status = StringField()
    log_id = StringField()

    def __str__(self):
        return self.tx_hash if self else ''
