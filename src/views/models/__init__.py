# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from unicodedata import category
from .nft import NftView
from .nft_detail import NftDetailView
from .collection import CollectionView
from .nft_history import NftHistoryView
from .order import OrderView
from .roles import RolesView
from .user import UserView
from .referral import ReferralView
from .promotion import PromotionView
from ...models.referral import Referral
from ...models.nft import Nft
from ...models.order import Order
from ...models.security import User, Role
from ...models.nft_detail import NftDetail

from ...models.collection import Collection

from ...models.nft_history import NftHistory

from ...models.promotion import Promotion


model_views = [
    UserView(User, category='Setting'),
    RolesView(Role, category='Setting'),

    OrderView(Order, category='NFT'),
    NftView(Nft, category='NFT'),
    NftDetailView(NftDetail, category='NFT'),

    ReferralView(Referral, category='Referral'),

    
    CollectionView(Collection , category='NFT'),
    
    NftHistoryView(NftHistory, category='NFT'),

    PromotionView(Promotion, category='Promotion')


]