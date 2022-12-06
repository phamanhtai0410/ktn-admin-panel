from src.views.base import MyBaseModelView
import pydash as py_
from markupsafe import Markup

class SettingView(MyBaseModelView):
    column_list = ['referral_cookies']
    can_edit = True
    can_create = False
    can_delete = False

    edit_modal = True

    def referral_cookies_format(view, context, model, name):
        return Markup(f'{py_.get(model, "referral_cookies", 0)} days')

    column_formatters = {
        'referral_cookies': referral_cookies_format,
    }