# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, IntField, FloatField

from src.models.base import BaseDocument


class NftsStatistic(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'nfts_statistics'
    }
    nft_type = IntField()
    rarity = IntField()
    contract = StringField()
    total = FloatField()


    def __str__(self):
        return self.nft_type if self else ''
