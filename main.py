import traceback

import sentry_sdk
from flask import Flask, g, url_for, render_template
from flask_admin import Admin, helpers
# from flask_security.utils import hash_password
from sentry_sdk.integrations.flask import FlaskIntegration

from src.config import Config
from src.extensions import db, security

app = Flask(__name__, template_folder='./src/templates/', static_folder='./src/static/', static_url_path='/static')
app.config.update(Config.__dict__)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

#
# @app.errorhandler(500)
# def server_error_page(error):
#     print(error)
#     return render_template('home/page-500.html'), 500


# Init database
db.init_app(app)
from src.models.security import UserDatastore
from src.views.base import MyAdminIndexView

security_ctx = security.init_app(app, UserDatastore)

admin = Admin(
    app=app,
    name=Config.PROJECT_NAME,
    template_mode=Config.TEMPLATE_MODE,
    base_template='my_master.html',
    index_view=MyAdminIndexView(),
    url='/'
)


@security_ctx.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=helpers,
        get_url=url_for
    )


# Flexible way for defining custom mail sending task.
@security_ctx.send_mail_task
def delay_flask_security_mail(msg):
    print(msg.body)
    sentry_sdk.capture_message(msg.body)
    # Create a user to test with


@app.before_first_request
def create_user():
    admin_root = app.config.get('ADMIN_ROOT')
    if not UserDatastore.find_user(email=admin_root):
        UserDatastore.create_user(email=admin_root,
                                  password="root",
                                  is_admin=True)


from src.views import blueprints

for _blueprint in blueprints:
    app.register_blueprint(_blueprint)

from src.views.models import model_views, model_categories
from src.views import pages
for _model_ca in model_categories.values():
    admin.add_category(**_model_ca)

for _model_view in model_views:
    admin.add_view(_model_view)


for _page in pages:
    admin.add_view(_page)

print(
    [x.url for x in admin._views]
)
# Init sentry
if Config.SENTRY_DSN:
    sentry_sdk.init(
        dsn=Config.SENTRY_DSN,
        integrations=[FlaskIntegration()],
        server_name=Config.PROJECT_NAME
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
