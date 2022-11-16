# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, IntField

from src.models.base import BaseDocument


class NftRarity(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'nft_rarities'
    }
    name = StringField(required=True)
    code = StringField()
    rarity_id = IntField()

    def __str__(self):
        return self.name if self else ''
