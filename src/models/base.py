# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
import datetime as dt
import traceback

from flask_login import current_user
from flask_mongoengine import Document
from mongoengine import DateTimeField

from src.extensions import db
# from src.models.admin_log import AdminLog


class BaseDocument(Document):
    meta = {
        'allow_inheritance': False,
        'abstract': True
    }

    created_time = DateTimeField(default=dt.datetime.now)
    created_by = db.StringField()

    updated_time = db.DateTimeField(default=dt.datetime.now)
    updated_by = db.StringField()

    def _save_create(self, doc, force_insert, write_concern):
        doc["created_time"] = dt.datetime.now()
        doc["updated_time"] = dt.datetime.now()
        if getattr(current_user, 'get_user_name', None):
            doc["created_by"] = current_user.get_user_name()
            doc["updated_by"] = current_user.get_user_name()
        # if hasattr(self, 'tracking') and self.tracking:
        #     #     model = StringField()
        #     #     action = StringField()
        #     #     before = DictField()
        #     #     after = DictField()
        #     #     created_by = StringField()
        #     #     created_time = DateTimeField(default=datetime.now)
        #     AdminLog(
        #         model=self.name,
        #         action='create',
        #         created_by=current_user.get_user_name(),
        #         created_time=dt.datetime.now(),
        #         before={},
        #         after=doc
        #     ).save(force_insert=True)
        return super()._save_create(doc, force_insert, write_concern)

    def _save_update(self, doc, save_condition, write_concern):
        doc["updated_time"] = dt.datetime.now()
        if getattr(current_user, 'get_user_name', None):
            doc["updated_by"] = current_user.get_user_name()
        # if hasattr(self, 'tracking') and self.tracking:
        #     # model = StringField()
        #     #     action = StringField()
        #     #     before = DictField()
        #     #     after = DictField()
        #     #     created_by = StringField()
        #     #     created_time = DateTimeField(default=datetime.now)
        #     print(self.name)
        #     AdminLog(
        #         model=self.name,
        #         action='update',
        #         created_by=current_user.get_user_name(),
        #         created_time=dt.datetime.now(),
        #         before=self.to_mongo(),
        #         after=doc
        #     ).save(force_insert=True)
        return super()._save_update(doc, save_condition, write_concern)

    def _get_update_doc(self):
        """Return a dict containing all the $set and $unset operations
        that should be sent to MongoDB based on the changes made to this
        Document.
        """
        updates, removals = self._delta()

        update_doc = {}
        if updates:
            updates["updated_time"] = dt.datetime.now()
            if getattr(current_user, 'get_user_name', None):
                updates["updated_by"] = current_user.get_user_name()
            update_doc["$set"] = updates
        if removals:
            update_doc["$unset"] = removals

        return update_doc

    @classmethod
    def update_by_query(cls, query, data):
        result = cls.objects(__raw__=query).update(**data)
        return result


class BaseDynamicDocument(db.DynamicDocument):
    meta = {
        'allow_inheritance': True,
        'abstract': True
    }

    created_time = db.DateTimeField()
    created_by = db.StringField()

    updated_time = db.DateTimeField()
    updated_by = db.StringField()

    def _save_create(self, doc, force_insert, write_concern):
        doc["created_time"] = dt.datetime.now()
        doc["updated_time"] = dt.datetime.now()
        if getattr(current_user, 'get_user_name', None):
            doc["created_by"] = current_user.get_user_name()
            doc["updated_by"] = current_user.get_user_name()

        return super()._save_create(doc, force_insert, write_concern)

    def _save_update(self, doc, save_condition, write_concern):
        doc["updated_time"] = dt.datetime.now()
        if getattr(current_user, 'get_user_name', None):
            doc["updated_by"] = current_user.get_user_name()
        return super()._save_update(doc, save_condition, write_concern)

    def _get_update_doc(self):
        """Return a dict containing all the $set and $unset operations
        that should be sent to MongoDB based on the changes made to this
        Document.
        """
        updates, removals = self._delta()

        update_doc = {}
        if updates:
            updates["updated_time"] = dt.datetime.now()
            if getattr(current_user, 'get_user_name', None):
                updates["updated_by"] = current_user.get_user_name()
            update_doc["$set"] = updates
        if removals:
            update_doc["$unset"] = removals

        return update_doc

    @classmethod
    def update_by_query(cls, query, data):
        result = cls.objects(__raw__=query).update(**data)
        return result
