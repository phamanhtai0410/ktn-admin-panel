from markupsafe import Markup
from flask_admin import BaseView, expose


class SettingSmcView(BaseView):

    @expose('/')
    def index(self):
        return self.render("pages/smc_setting.html")
