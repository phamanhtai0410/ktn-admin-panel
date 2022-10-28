from markupsafe import Markup
from src.views.base import MyBaseModelView
from src.config import Config


class NftHistoryView(MyBaseModelView):
    column_list = ['token_id', 'contract', 'from_address', 'to_address', 'event', 'tx_hash', 'block_number', 'created_time']
    can_edit = False
    can_create = False
    can_delete = False
    
    def contract_formart(view, context, model, name):
        _contract = model['contract']
        return Markup(f'<a target="_blank"  href="{Config.BSC_SCAN}/token/{_contract}">{_contract}</a>')
    
    def from_address_formart(view, context, model, name):
        _address = model['from_address']
        return Markup(f'<a target="_blank"  href="{Config.BSC_SCAN}/address/{_address}">{_address[:4]}...{_address[-4:]}</a>')

    def to_address_formart(view, context, model, name):
        _address = model['to_address']
        return Markup(f'<a target="_blank"  href="{Config.BSC_SCAN}/address/{_address}">{_address[:4]}...{_address[-4:]}</a>')
    
    def tx_hash_formart(view, context, model, name):
        _tx_hash = model.tx_hash
        if isinstance(_tx_hash, str) and len(_tx_hash) > 12:
            return Markup(
                f'<a target="_blank"  href="{Config.BSC_SCAN}/tx/{_tx_hash}">{_tx_hash[:4]}...{_tx_hash[-4:]}</a>')
        return Markup("<p style='color: #808080;'>WAITING</p>")

    column_searchable_list = ['contract']

    column_default_sort = ('block_number', True)
    column_formatters = {
        'contract' : contract_formart,
        'from_address': from_address_formart,
        'to_address': to_address_formart,
        'tx_hash': tx_hash_formart
    }

