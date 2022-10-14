# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from mongoengine import StringField, ListField, EmbeddedDocumentField, IntField, FloatField

from src.extensions import db
from src.models.base import BaseDocument


class Item(db.EmbeddedDocument):
    meta = {'strict': False}

    name = StringField()
    rarity = StringField()
    amount = IntField()
    price = FloatField()

    def __str__(self):
        return self.name if self else ''


class Order(BaseDocument):
    meta = {
        'strict': False,
        'collection': 'orders'
    }
    address = StringField()
    order_id = StringField()
    items = ListField(EmbeddedDocumentField(Item))
    status = StringField()

    def __str__(self):
        return self.order_id if self else ''
