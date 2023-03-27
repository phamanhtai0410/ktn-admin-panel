from src.views.base import MyBaseModelView, RowActionListMixin
from markupsafe import Markup
from datetime import datetime

class RaffleConfigView(MyBaseModelView, RowActionListMixin):
    # View column
    column_list = [
        'name',
        'start_time',
        'end_time',
        'point_per_task'
    ]
    
    can_delete = True
    
    column_searchable_list = ['name']
    column_default_sort = ('created_time', True)

    def _start_time_formatter(view, context, model, name):
        _start_time = datetime.fromtimestamp(model['start_time'])
        return Markup(
            f'<p>{_start_time}</p>'
        )
    
    def _end_time_formatter(view, context, model, name):
        _end_time = datetime.fromtimestamp(model['end_time'])
        return Markup(
            f'<p>{_end_time}</p>'
        )
        
    column_formatters = {
        'start_time': _start_time_formatter,
        'end_time': _end_time_formatter
    }