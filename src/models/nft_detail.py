# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, IntField, BooleanField, FloatField

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
    discount = FloatField(min_value=0, max_value=100)
    commission = FloatField(min_value=0, max_value=100)
    is_show = BooleanField()

    def __str__(self):
        return self.nft_id if self else ''

    def tracking(self):
        return True
