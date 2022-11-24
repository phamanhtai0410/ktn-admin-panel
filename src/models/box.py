# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, BooleanField, ListField, EmbeddedDocument, IntField, FloatField, EmbeddedDocumentField

from src.models.base import BaseDocument


class NFTRare(EmbeddedDocument):
    nft_id = IntField(required=True)
    proportion = IntField(required=True)


class Box(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'boxes'
    }

    box_id = IntField(required=True, unique=True)

    address = StringField()
    name = StringField(required=True)
    symbol = StringField(required=True)
    collection = StringField(required=True)
    # nfts = ListField(EmbeddedDocumentField(NFTRare))
    description = StringField(required=True)
    image = StringField(required=True)
    price = IntField(required=True)
    discount = FloatField(min_value=0, max_value=100)
    commission = FloatField(min_value=0, max_value=100)
    commission_level_2 = FloatField(min_value=0, max_value=100)
    active = BooleanField(default=False)
    block_number = IntField()

    def __str__(self):
        return self.address if self else ''
