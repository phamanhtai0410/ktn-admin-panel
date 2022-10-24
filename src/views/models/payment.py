from markupsafe import Markup
from src.views.base import MyBaseModelView
from src.config import Config


class PaymentView(MyBaseModelView):
    column_list = ['asset', 'chain', 'chain_id', 'asset_logo', 'chain_logo', 'is_active', 'created_time']
    can_edit = True
    can_create = True
    can_delete = True
    
    column_searchable_list = ['asset']

    column_default_sort = ('created_time', True)
    def asset_logo_format( view, context, model , name):
        return Markup(f'<a target="_blank" href="{model["asset_logo"]}"> logo </a>')
    
    def chain_logo_format( view, context, model , name):
        return Markup(f'<a target="_blank" href="{model["chain_logo"]}"> logo </a>')
    
    column_formatters = {
        'asset_logo': asset_logo_format,
        'chain_logo': chain_logo_format
        
    }

