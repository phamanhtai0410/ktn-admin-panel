from src.views.base import MyBaseModelView, RowActionListMixin

class RaffleView(MyBaseModelView, RowActionListMixin):
     # View column
    column_list = [
        'address',
        'email',
        'user_id_twitter',
        'is_favourite_twitter',
        'is_retweeted_twitter',
        'is_follow_twitter',
        'is_join_discord',
        'count_referrals',
        'entries',
        'created_time'
    ]

    action_disallowed_list = ['create', 'delete']
    
    can_edit = False
    can_create = False
    can_delete = False

    column_searchable_list = ['address', 'user_id_twitter', 'email']

    column_default_sort = ('created_time', True)