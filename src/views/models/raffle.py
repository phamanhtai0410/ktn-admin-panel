from src.views.base import MyBaseModelView, RowActionListMixin
from markupsafe import Markup
from datetime import datetime

class RaffleView(MyBaseModelView, RowActionListMixin):
    # View column
    column_list = [
        'address',
        'user_id_twitter',
        'is_favourite_twitter',
        'is_retweeted_twitter',
        'is_follow_twitter',
        'is_join_discord',
        'count_referrals',
        'entries',
        'created_time'
    ]
    
    can_delete = False
    can_create = False
    can_edit = False
    
    
    column_searchable_list = ['address']
    column_default_sort = ('created_time', True)

    # def _time_formatter(view, context, model, name):
    #     _start_time = datetime.fromtimestamp(model['created_time'])
    #     return Markup(
    #         f'<p>{_start_time}</p>'
    #     )
        
    # column_formatters = {
    #     'created_time': _time_formatter
    # }