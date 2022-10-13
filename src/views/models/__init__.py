# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from .roles import RolesView
from .user import UserView
from ...models.security import User, Role

model_views = [
    UserView(User, category='Setting'),
    RolesView(Role, category='Setting')
]
