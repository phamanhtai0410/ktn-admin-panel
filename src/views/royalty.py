import requests
from flask import request, render_template, redirect
from flask_login import current_user
from flask_security.utils import hash_password
from flask_admin import BaseView, expose

from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, validators

from src.config import Config
from src.models.security import User
from src.utils.s3_image_uploader import S3ImageUploadField


class RoyaltyView(BaseView):

    # @expose('/', methods=['GET'])
    # def index(self):
    #     return redirect("/admin")

    @expose('/', methods=['GET', 'POST'])
    def index(self):
        # res = requests.get(f'{Config.DAPP_API}/royalty_info', timeout=10)
        # print("** Call to get Royalty Infos: ",res.text)
        return self.render('pages/royalty.html',
                           ROYALTY_CONTROLLER_ADDRESS=Config.ROYALTY_CONTROLLER_ADDRESS
                           )

