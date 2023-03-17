# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, BooleanField, IntField
from src.models.base import BaseDocument


class Raffle(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'raffle'
    }
    address = StringField(required=True)
    user_id_twitter = StringField(required=True)
    is_favourite_twitter = BooleanField(required=True)
    is_retweeted_twitter = BooleanField(required=True)
    is_follow_twitter = BooleanField(required=True)
    is_join_discord = BooleanField(required=True)
    count_referrals = IntField(required=True)
    entries = IntField(required=True)

