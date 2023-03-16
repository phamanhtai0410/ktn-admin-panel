# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, IntField, ListField, DictField, BooleanField, \
    FloatField, EmbeddedDocument, EmbeddedDocumentField
from src.models.base import BaseDocument


class NftType(EmbeddedDocument):
    AssetID = StringField(required=True)
    DataTableID = StringField(required=True)
    AssetDescription = StringField(required=False)
    AssetRarity = StringField(required=True)
    EventDataTableID = StringField(required=False)
    AssetUniqueIndex = StringField(required=False)
    ImageUrl = StringField(required=False)
    AnimationModelUrl = StringField(required=False)
    rate = FloatField(required=True)

class NftCollection(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'collection'
    }
    collection_id = IntField(required=True, unique=True)
    name = StringField(required=True)
    symbol = StringField(required=True)
    description = StringField(required=True)
    image = StringField(required=True)
    address = StringField()
    # max_rarity = IntField(default=0)
    block_number = IntField()
    # delist = BooleanField(default=False)
    disable_mint = BooleanField(default=False)
    royalty_rate = IntField(required=True, default=20, min_value=0, max_value=100)
    total_supply = IntField(required=True,default=10000, min_value=1)
    
    types_list = ListField(EmbeddedDocumentField(NftType))
    deployed = BooleanField(required=True)


    def __str__(self):
        return self.name if self else ''
