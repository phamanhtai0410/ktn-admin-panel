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

