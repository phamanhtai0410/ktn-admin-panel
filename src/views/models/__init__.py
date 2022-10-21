# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from unicodedata import category

from .exchange import ExchangeView
from .minted_nfts import MintedNftsView
from .nft_detail import NftDetailView
from .nft_type import NftTypeView
from .nft_history import NftHistoryView
from .order import OrderView
from .point import PointView
from .roles import RolesView
from .user import UserView
from .user_app import UserAppView
from .referral import ReferralView
from .promotion import PromotionView
from .nfts_statistic import NftsStatisticView
from .referral_reward_config import ReferralRewardConfigView
from ...models.exchange import ExchangeLog
from ...models.point import PointLog

from ...models.referral import Referral
from ...models.minted_nfts import MintedNfts
from ...models.order import Order
from ...models.security import User, Role
from ...models.user import UserApp
from ...models.nft_detail import NftDetail
from ...models.nft_type import NftType

from ...models.nft_history import NftHistory

from ...models.promotion import Promotion
from ...models.nfts_statistic import NftsStatistic
from ...models.referral_reward_config import ReferralRewardConfig

model_views = [
    UserView(User, category='Setting'),
    RolesView(Role, category='Setting'),

    OrderView(Order, category='NFT'),
    MintedNftsView(MintedNfts, category='NFT'),
    UserAppView(UserApp, category='Application'),
    NftDetailView(NftDetail, category='NFT'),
    NftsStatisticView(NftsStatistic, category='NFT'),

    ReferralView(Referral, category='Referral'),
    ReferralRewardConfigView(ReferralRewardConfig, category='Referral'),

    NftTypeView(NftType, category='NFT'),

    NftHistoryView(NftHistory, category='NFT'),

    PromotionView(Promotion, category='Promotion'),
    ExchangeView(ExchangeLog, category="Point"),
    PointView(PointLog, category='Point')

]
