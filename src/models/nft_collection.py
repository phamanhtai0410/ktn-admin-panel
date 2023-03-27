# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, IntField, ListField, BooleanField, \
    FloatField, EmbeddedDocument, EmbeddedDocumentField
from src.models.base import BaseDocument


class NftType(EmbeddedDocument):
    AssetID = StringField(required=True)
    DataTableID = StringField(required=True)
    AssetDescription = StringField(required=False)
    AssetRarity = StringField(required=True)
    EventDataTableID = StringField(required=False)
    AssetUniqueIndex = StringField(required=False)
    ImageUrl = StringField(required=False, default='', missing='')
    AnimationModelUrl = StringField(required=False, default='', missing='')
    rate = FloatField(required=True)
    price = FloatField(required=True)

class Royalty(EmbeddedDocument):
    user_address = StringField(required=True)
    percent = FloatField(required=True, min_value=0, max_value=100)


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
    block_number = IntField(default=0)
    # delist = BooleanField(default=False)
    disable_mint = BooleanField(default=False)
    total_supply = IntField(required=True, default=10000, min_value=1)

    types_list = ListField(EmbeddedDocumentField(NftType))
    royalty = ListField(EmbeddedDocumentField(Royalty))

    commision = FloatField(required=True)
    commision_level_2 = FloatField(required=True)

    deployed = BooleanField(default=False)
    royalty_rate = IntField(required=True, default=20, min_value=0, max_value=100)
    treasury_address = StringField()

    chain_id = IntField(required=False, default=None)
    chain = StringField(required=False, default=None)
    pay_token_address = StringField(required=False, default=None)
    dapp_creator_address = StringField(required=False, default=None)

    def __str__(self):
        return self.name if self else ''
