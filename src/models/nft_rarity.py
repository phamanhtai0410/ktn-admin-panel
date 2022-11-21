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
    rarity_id = IntField()
    collection_id = IntField()
    collection_address = StringField()

    def __str__(self):
        return self.name if self else ''
