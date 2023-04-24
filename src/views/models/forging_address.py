import random
import string

from flask import request, redirect, flash, redirect, url_for
from flask_admin import expose
from mongoengine import DoesNotExist

from src.views.base import MyBaseModelView, RowActionListMixin
from src.models.nft_collection import NftCollection


class ForgingAddressView(RowActionListMixin, MyBaseModelView):
    column_list = ['chain', 'collection_type', 'collection_address']
    can_edit = True
    can_create = True
    can_delete = True

    column_default_sort = ('created_time', True)

    def create_model(self, form):
        collection_address = form.collection_address.data
        chain = form.chain.data

        for address in collection_address:
            try:
                _collection = NftCollection.objects.get(address=address.lower(), chain=chain)
                super().create_model(form)
                return True
            except:
                flash(f'Nft collection not found or not correct chain')
                return False