# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, IntField, FloatField

from src.models.base import BaseDocument


class ReferralRewardConfig(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'referral_reward_config'
    }
    nft_type = IntField()
    rarity = IntField()
    reward_percent = FloatField()

    def __str__(self):
        return self.nft_type if self else ''
