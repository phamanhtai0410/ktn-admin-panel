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
    present = FloatField(required=True)
    max_item = IntField(required=True)


class Box(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'boxes'
    }
    address = StringField()
    active = BooleanField(default=False)
    name = StringField()
    collection = StringField()
    nfts = ListField(EmbeddedDocumentField(NFTRare))
    description = StringField()
    image = StringField()
    price = IntField()
    discount = FloatField(min_value=0, max_value=100)
    commission = FloatField(min_value=0, max_value=100)

    def __str__(self):
        return self.address if self else ''
