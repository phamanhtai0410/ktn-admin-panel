from markupsafe import Markup
from wtforms import validators

from src.config import Config
from src.views.base import MyBaseModelView


class NFTDetailView(MyBaseModelView):
    column_list = ['nft_id', 'name', 'rarity', 'type', 'description', 'image', 'price']
    can_edit = False
    can_create = False
    can_delete = False

    column_default_sort = ('nft_id', False)

