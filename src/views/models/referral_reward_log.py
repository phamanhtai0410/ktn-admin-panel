from markupsafe import Markup
from wtforms import validators
import pydash as py_ 

from src.config import Config
from src.views.base import MyBaseModelView


class ReferralRewardLogView(MyBaseModelView):
    column_list = ['address', 'point', 'nft_data', 'reward_type']
    can_edit = False
    can_create = False
    can_delete = False


    column_searchable_list = ['address']

    def nft_data_format(view, context, model, name):
        _nft_data = py_.get(model, 'nft_data')
        _tx_hash = py_.get(_nft_data, 'tx_hash')
        _token_id = py_.get(_nft_data, 'token_id')
        _nft_type = py_.get(_nft_data, 'nft_type')
        _rarity = py_.get(_nft_data, 'rarity')

        return Markup(f"<ul><li>tx_hash: {_tx_hash}</li><li>token_id: {_token_id}</li><li>nft_type: {_nft_type}</li><li>rarity: {_rarity}</li></ul>")

    def point_format(view, context, model, name):
        return Markup(f'{py_.get(model, "point", 0)} point')

    column_formatters = {
        'point': point_format,
        'nft_data': nft_data_format
    }