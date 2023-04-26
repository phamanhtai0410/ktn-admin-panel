import random
import string
import traceback

from flask import request, redirect, url_for, flash, send_file
from flask_admin import expose
import pydash as py_
import web3
from wtforms import validators, fields

from src.models.pre_launch_nft_whitelist import PreLaunchNftWhitelist
from src.views.base import MyBaseModelView, RowActionListMixin


class PreLaunchNftWhitelistView(RowActionListMixin, MyBaseModelView):
    column_list = ['address']
    can_edit = True
    can_create = True
    can_delete = True

    # column_searchable_list = ['address', 'collection']

    list_template = 'form/models/pre_launch_nft_whitelist/menu_bar.html'

    column_default_sort = ('collection', True)

    form_args = {
        'address': {
            'validators': [validators.required()]
        }
    }

    def is_valid_data(self, data, is_upload_file=False, csv_row=0):
        print('Check is valid')
        _web3 = web3.Web3()
        _address = py_.get(data, 'address', None)
        if not _address or not _web3.isAddress(_address):
            if is_upload_file:
                flash(message=f'DATA NOT VALID - ROW IN CSV: {csv_row + 1} - address: {_address}', category="error")
            else:
                flash(message=f'DATA NOT VALID - address: {_address}', category="error")
                
            return False

        return True

    @expose('/upload_pre_launch_whitelist', methods=['POST'])
    def upload_pre_launch_whitelist(self):
        file = request.files.get('files')
        print(file)
        _csv_data = file.read().decode('utf-8')
        if not _csv_data:
            flash(message=f'Do not have data', category="error")

        _web3 = web3.Web3()
        _csv_data = _csv_data.split('\n')
        _insert_data = []
        for (_row, _item) in enumerate(_csv_data):
            # NOTE: row == 0 is row name of data
            if _row == 0:
                continue
            
            _data = _item.split(',')
            print(len(_csv_data), len(_data), _data, _row)

            _address = py_.get(_data, '0', None)
            
            if len(_data) != 3:
                _insert = {
                    'address': None
                }
            else:
                _insert = {
                    'address': _address.lower()
                }
            _is_valid = self.is_valid_data(
                data=_insert,
                is_upload_file=True,
                csv_row=_row
            )

            if not _is_valid:
                return redirect(url_for('.index_view'))
            
            _insert_data.append(_insert)

        # NOTE: loop in insert_data for update amount, address if upload file many time
        for _item in _insert_data:
            _address = py_.get(_item, 'address')
            PreLaunchNftWhitelist.objects(address=_address).update_one(
                set__address=_address,
                upsert=True)


        return redirect(url_for('.index_view'))

    @expose('/download_example', methods=['GET'])
    def download_example(self):
        return send_file('uploads/pre_launch_whitelist_address_example.csv')
