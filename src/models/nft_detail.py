# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, IntField, BooleanField, FloatField

from src.models.base import BaseDocument

from src.enums.nft_type import NftType, NftRarity

class NftDetail(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'nft_details'
    }
    nft_id = IntField(unique=True, required=True)
    name = StringField(required=True)
    rarity = IntField(unique_with='nft_id')
    type = IntField()
    description = StringField()
    image = StringField()
    price = IntField()
    discount = FloatField(min_value=0, max_value=100)
    commission = FloatField(min_value=0, max_value=100)
    commission_level_2 = FloatField(min_value=0, max_value=100)
    is_show = BooleanField()

    def __str__(self):
        return self.name if self else ''

    def tracking(self):
        return True
