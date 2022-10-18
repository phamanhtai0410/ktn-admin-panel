# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, IntField

from src.models.base import BaseDocument


class NftDetail(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'nft_details'
    }
    nft_id = IntField()
    name = StringField()
    rarity = IntField()
    type = IntField()
    description = StringField()
    image = StringField()
    price = IntField()

    def __str__(self):
        return self.nft_id if self else ''
