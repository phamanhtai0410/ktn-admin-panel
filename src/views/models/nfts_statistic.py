from markupsafe import Markup
from wtforms import validators

from src.config import Config
from src.views.base import MyBaseModelView


class NftsStatisticView(MyBaseModelView):
    column_list = ['nft_type', 'rarity', 'contract', 'total', 'updated_time']

    can_edit = False
    can_create = False
    can_delete = False

    list_template = 'custom/nfts_statistic.html'

    column_default_sort = [('nft_type', False), ('rarity', False)]