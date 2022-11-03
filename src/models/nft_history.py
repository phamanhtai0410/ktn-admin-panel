# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from tokenize import String
from mongoengine import StringField, IntField

from src.models.base import BaseDocument


class NftHistory(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'nfts_history'
    }
    token_id = IntField()
    contract = StringField()
    from_address = StringField()
    to_address = StringField()
    event = StringField()
    tx_hash = StringField()
    block_number = IntField()

    def __str__(self):
        return self.token_id if self else ''

