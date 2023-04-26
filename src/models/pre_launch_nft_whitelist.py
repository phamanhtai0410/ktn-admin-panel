# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, IntField
import web3

from src.models.base import BaseDocument

class PreLaunchNftWhitelist(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'pre_launch_nft_whitelist'
    }

    address = StringField(required=True) # Address of user
    # amount = IntField(required=True) # Address amount of nft can mint in each whitelist phase
    # collection = StringField(required=True) # Address of collection 