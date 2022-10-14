# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from .nft import NFTView
from .order import OrderView
from .roles import RolesView
from .user import UserView
from ...models.nft import NFT
from ...models.order import Order
from ...models.security import User, Role

model_views = [
    UserView(User, category='Setting'),
    RolesView(Role, category='Setting'),
    OrderView(Order, category='NFT'),
    NFTView(NFT, category='NFT')
]
