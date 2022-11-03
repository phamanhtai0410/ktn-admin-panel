from markupsafe import Markup
from wtforms import validators
import pydash as py_ 

from src.config import Config
from src.views.base import MyBaseModelView


class ReferralRewardConfigView(MyBaseModelView):
    column_list = ['nft_type', 'rarity', 'reward_percent']
    can_edit = True
    can_create = True
    can_delete = True

    column_default_sort = ('nft_type', False)

    def reward_percent_format(view, context, model, name):
        return Markup(f'{py_.get(model, "reward_percent", 0)} %')

    column_formatters = {
        'reward_percent': reward_percent_format,
    }