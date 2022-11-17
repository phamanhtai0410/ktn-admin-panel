import requests
from flask import request, render_template, redirect
from flask_login import current_user
from flask_security.utils import hash_password
from markupsafe import Markup
from flask_admin import BaseView, expose
from pydash import get

from src.abis import nft_abi, staking_abi, creator_abi
from src.config import Config
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators, SubmitField, PasswordField, validators

from src.models.security import User
from src.utils.s3_image_uploader import S3ImageUploadField


class ProfileForm(FlaskForm):
    password = PasswordField('Password', [validators.required(), validators.Length(min=6)])
    password2 = PasswordField('Confirm password', [validators.required(), validators.Length(min=6)])
    submit = SubmitField('Submit')


class ProfileView(BaseView):

    # @expose('/', methods=['GET'])
    # def index(self):
    #     return redirect("/admin")

    @expose('/', methods=['GET', 'POST'])
    def index(self):
        print(current_user)
        # user = User.get_by_email(current_user)
        # print('user', user)
        if request.method == 'POST':
            _form = request.form.to_dict()
            form = ProfileForm(obj=_form)
            if not form.validate():
                print('_form', form.validate())
                return self.render('pages/profile.html', form=form)

            print('_form', _form)
            if form.password.data and form.password.data != form.password2.data:
                form.password.errors.append('Password not matched')
                form.password2.errors.append('Password not matched')
                return self.render('pages/profile.html', form=form)
            if form.password.data:
                password = hash_password(form.password.data)
                print("set user password", password, current_user, type(current_user))

                User.objects(email=current_user.get_user_name()).update(set__password=password)

            return redirect("/admin")
        form = ProfileForm(obj={})

        return self.render('pages/profile.html', form=form)

    def is_visible(self):
        return False
