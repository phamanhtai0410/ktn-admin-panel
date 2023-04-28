from markupsafe import Markup
from wtforms import validators

from src.config import Config
from src.views.base import MyBaseModelView


class EmailSubscribeView(MyBaseModelView):
    column_list = ['email']
    can_edit = False
    can_create = False
    can_delete = False
