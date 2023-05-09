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

class WhitelistTime(EmbeddedDocument):
    phase = IntField(required=True)
    start_time = IntField(required=True)
    end_time = IntField(required=True)
    is_public = BooleanField(default=False)

class NftCollection(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'collection'
    }
    collection_id = IntField(required=True, unique=True)
    name = StringField(required=True)
    symbol = StringField(required=True)
    description = StringField(required=True)
    image = StringField(required=False)
    address = StringField()
    # max_rarity = IntField(default=0)
    block_number = IntField(default=0)
    # delist = BooleanField(default=False)
    disable_mint = BooleanField(default=False)
    total_supply = IntField(required=True, default=10000, min_value=1)

    types_list = ListField(EmbeddedDocumentField(NftType))
    royalty = ListField(EmbeddedDocumentField(Royalty))

    commission = FloatField(required=True)
    commission_level_2 = FloatField(required=True)

    discount = FloatField(required=True)

    deployed = BooleanField(default=False)
    royalty_rate = IntField(required=True, default=20, min_value=0, max_value=100)
    treasury_address = StringField()

    chain_id = IntField(required=False, default=None)
    chain = StringField(required=False, default=None)
    
    pay_token_symbol = StringField(required=False, default=None)
    pay_token_address = StringField(required=False, default=None)
    is_paid_by_native = BooleanField(required=False)
    dapp_creator_address = StringField(required=False, default=None)

    whitelist_time = ListField(EmbeddedDocumentField(WhitelistTime), default=[], missing=[])
    whitelist_price = FloatField(required=False, missing=0)

    is_box = BooleanField()
    box_image_url = StringField(required=False)

    is_existing_metadata = BooleanField(required=False, default=False)
    price = FloatField(required=False, default=0)
    image_base_url = StringField(required=False, default='')
    json_base_url = StringField(required=False, default='')
    display_url = StringField(required=False, default='')

    def __str__(self):
        return self.name if self else ''
