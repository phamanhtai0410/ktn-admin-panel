# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, IntField, BooleanField, FloatField, EmbeddedDocument, \
    EmbeddedDocumentField, \
    ListField, ReferenceField

from src.models.base import BaseDocument
from src.models.variable import Variable


class NftAttribute(EmbeddedDocument):
    id = IntField()
    value = IntField()


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
    metadata_cid = StringField()

    def __str__(self):
        return self.name if self else ''

