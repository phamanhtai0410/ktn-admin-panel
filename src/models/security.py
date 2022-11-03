# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from flask_login import UserMixin
from flask_mongoengine import Document
from flask_security import MongoEngineUserDatastore, RoleMixin
from flask_security.utils import hash_password, verify_password
from mongoengine import StringField

from src.extensions import db
from src.models.base import BaseDocument
from src.routes import ROLES_PAGE_ACCESS


class Site(Document):
    meta = {'collection': 'sites'}

    id = db.StringField(max_length=20, primary_key=True, required=True)
    name = db.StringField(max_length=20, required=True)

    def __unicode__(self):
        return self.id


class PageAction(db.EmbeddedDocument):
    meta = {'strict': False}

    edit = db.BooleanField(default=False)
    create = db.BooleanField(default=False)
    delete = db.BooleanField(default=False)
    export = db.BooleanField(default=False)
    view_details = db.BooleanField(default=False)


class Accessible(db.EmbeddedDocument):
    meta = {'strict': False}

    page = db.StringField(choices=ROLES_PAGE_ACCESS)
    action = db.EmbeddedDocumentField(PageAction)


class Role(BaseDocument, RoleMixin):
    meta = {'strict': False}
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)
    access = db.ListField(db.EmbeddedDocumentField(Accessible))

    def __str__(self):
        return self.name if self else ''


class User(BaseDocument, UserMixin):
    meta = {'strict': False, 'collection': 'admin_users'}
    active = db.BooleanField(default=True)
    is_admin = db.BooleanField(default=False)
    # username = db.StringField(max_length=255, unique=True)
    password = StringField()
    email = db.StringField(max_length=255, unique=True)
    # confirmed_at = db.DateTimeField()
    roles = db.ListField(db.ReferenceField(Role), default=[])

    def _save_create(self, doc, force_insert, write_concern):
        doc["password"] = hash_password(doc["password"])
        return super()._save_create(doc, force_insert, write_concern)

    # def verify_password(self, password):
    #     return verify_password(password=password, password_hash=self.password)
    #
    # @property
    # def password(self):
    #     raise AttributeError('password not readable')
    #
    # @password.setter
    # def password(self, password):
    #     if not password:
    #         password = "000000"
    #     self.password = hash_password(password)

    # Required for administrative interface
    def __unicode__(self):
        return self.get_user_name()

    def get_user_name(self):
        return self.email


UserDatastore = MongoEngineUserDatastore(db, User, Role)
