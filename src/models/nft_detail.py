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
    rarity = IntField()
    rarity_code = StringField(required=True, unique_with='nft_id')

    collection_id = IntField()
    description = StringField()
    image = StringField()
    price = IntField()
    discount = FloatField(min_value=0, max_value=100)
    commission = FloatField(min_value=0, max_value=100)
    is_show = BooleanField(default=True)
    address = StringField()

    def __str__(self):
        return self.name if self else ''

    def tracking(self):
        return True
