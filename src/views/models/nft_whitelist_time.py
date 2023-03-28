import random
import string
import traceback

from markupsafe import Markup
import datetime

from flask import request, redirect, url_for, flash
from flask_admin import expose
import pydash as py_
import web3
from wtforms import validators, fields

from src.models.nft_whitelist import NftWhitelist
from src.views.base import MyBaseModelView, RowActionListMixin


class NftWhitelistTimeView(MyBaseModelView):
    column_list = ['collection_id', 'name', 'symbol', 'address', 'whitelist_time']
    # can_edit = True
    can_create = False
    can_delete = False

    form_edit_rules = ('whitelist_time', )


    def whitelist_time_format(view, context, model, name):
        _whitelist_time = py_.get(model, 'whitelist_time', [])
        if not _whitelist_time:
            return ''
        _html = ''
        _whitelist_time = sorted(_whitelist_time, key=lambda x: py_.get(x, 'phase'))
        for _item in _whitelist_time:
            _phase = py_.get(_item, 'phase')
            _start_time = py_.get(_item, 'start_time')
            _end_time = py_.get(_item, 'end_time')
            _html += f'''
                Phase: {_phase}
                    <ul>
                        <li>
                            StartTime: {_start_time} - {datetime.datetime.fromtimestamp(_start_time).strftime('%Y/%m/%d %H:%m')}
                        </li>
                        <li>
                            EndTime: {_end_time} - {datetime.datetime.fromtimestamp(_end_time).strftime('%Y/%m/%d %H:%m')}
                        </li>
                    </ul>
            '''


        return Markup(_html)

    column_formatters = {
        'whitelist_time': whitelist_time_format,
    }


