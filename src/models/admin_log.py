# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from datetime import datetime

from mongoengine import StringField, DictField, Document, DateTimeField


class AdminLog(Document):
    meta = {
        'strict': False,
        'collection': 'admin_logs'
    }
    model = StringField()
    action = StringField()
    before = DictField()
    after = DictField()
    created_by = StringField()
    created_time = DateTimeField(default=datetime.now)

    def __str__(self):
        return self.model if self else ''
