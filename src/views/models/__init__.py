# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from unicodedata import category

from flask_admin.consts import ICON_TYPE_FONT_AWESOME

from src.models.payment import Payment

from src.views.models.payment import PaymentView
from .box import BoxView

from .exchange import ExchangeView
from .mesh_material import MeshMaterialView
from .minted_nfts import MintedNftsView
from .nft_collection import NftCollectionView
from .nft_mesh import MeshView
from .nft_rarity import NftRarityView
from .nft_history import NftHistoryView
from .order import OrderView
from .point import PointView
from .rate_box import RateBoxView
from .roles import RolesView
from .royalty import RoyaltyConfigView
from .user import UserView
from .user_app import UserAppView
from .referral import ReferralView
from .promotion import PromotionView
from .nfts_statistic import NftsStatisticView
from .referral_reward_config import ReferralRewardConfigView
from ...models.box import Box
from .setting import SettingView
from ...models.box_rate import RateOfBox

from ...models.exchange import ExchangeLog
from ...models.mesh_material import MeshMaterial
from ...models.nft_collection import NftCollection
from ...models.nft_mesh import Mesh
from ...models.point import PointLog

from ...models.referral import Referral
from ...models.minted_nfts import MintedNfts
from ...models.order import Order
from ...models.royalty import Royalty
from ...models.security import User, Role
from ...models.setting import Setting
from ...models.user import UserApp
from ...models.nft_rarity import NftRarity

from ...models.nft_history import NftHistory

from ...models.promotion import Promotion
from ...models.nfts_statistic import NftsStatistic

model_categories = {
    'Setting': {
        'name': 'Setting',
        'icon_type': ICON_TYPE_FONT_AWESOME,
        'icon_value': 'fa-cog fa-red'
    },
    'NFT': {
        'name': 'NFT',
        'icon_type': ICON_TYPE_FONT_AWESOME,
        'icon_value': 'fa-book'
    },
    'Master Data': {
        'name': 'Master Data',
        'icon_type': ICON_TYPE_FONT_AWESOME,
        'icon_value': 'fa-database'
    },
    'Application': {
        'name': 'Application',
        'icon_type': ICON_TYPE_FONT_AWESOME,
        'icon_value': 'fa-desktop'
    },
    'Payment': {
        'name': 'Payment',
        'icon_type': ICON_TYPE_FONT_AWESOME,
        'icon_value': 'fa-money'
    }
}
model_views = [
    UserView(User, category='Setting',
             menu_icon_type=ICON_TYPE_FONT_AWESOME, menu_icon_value='fa-circle'),
    RolesView(Role, category='Setting'),
    SettingView(Setting, category='Setting'),

    OrderView(Order, category='NFT'),
    MintedNftsView(MintedNfts, category='NFT'),
    UserAppView(UserApp, category='Application'),
    NftsStatisticView(NftsStatistic, category='NFT'),

    ReferralView(Referral, category='Application'),
    # ReferralRewardConfigView(ReferralRewardConfig, category='Referral'),

    NftHistoryView(NftHistory, category='NFT'),
    RoyaltyConfigView(Royalty, category='NFT'),
    PromotionView(Promotion, category='Application'),
    ExchangeView(ExchangeLog, category="Payment"),
    PointView(PointLog, category='Payment'),

    PaymentView(Payment, category='Payment'),
    NftCollectionView(NftCollection, category='Master Data'),

    NftRarityView(NftRarity, category='Master Data'),
    MeshView(Mesh, name="Mesh", category='Master Data'),
    BoxView(Box, category='Master Data'),
    RateBoxView(RateOfBox, category='Master Data'),
    MeshMaterialView(MeshMaterial, category='Master Data')
]
