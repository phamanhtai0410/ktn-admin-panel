# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, IntField, FloatField, EmbeddedDocumentField, ListField

from src.extensions import db
from src.models.base import BaseDocument

class NftDataItem(db.EmbeddedDocument):
    meta = {'strict': False}

    tx_hash = StringField()
    token_id = IntField()
    nft_type = IntField()
    rarity = IntField()

class ReferralRewardLog(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'referral_reward_log'
    }
    
    nft_data = EmbeddedDocumentField(NftDataItem)
    address = StringField()
    point = FloatField()
    reward_type = StringField()

