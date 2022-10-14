# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, IntField

from src.models.base import BaseDocument


class NFT(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'nfts'
    }
    address = StringField()
    token_id = StringField()
    rarity = IntField()

    def __str__(self):
        return self.token_id if self else ''
