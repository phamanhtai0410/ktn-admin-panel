# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, IntField

from src.models.base import BaseDocument


class NftType(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'nft_types'
    }
    type_id = IntField()
    name = StringField()
    description = StringField()
    image = StringField()
    max_rarity = IntField(required=True)

    def __str__(self):
        return self.name if self else ''
