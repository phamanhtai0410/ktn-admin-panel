# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from .nft import NftView
from .order import OrderView
from .roles import RolesView
from .user import UserView
from .user_app import UserAppView
from ...models.nft import Nft
from ...models.order import Order
from ...models.security import User, Role
from ...models.user import UserApp

model_views = [
    UserView(User, category='Setting'),
    RolesView(Role, category='Setting'),
    OrderView(Order, category='NFT'),
    NftView(Nft, category='NFT'),
    UserAppView(UserApp, category='Application')
]
