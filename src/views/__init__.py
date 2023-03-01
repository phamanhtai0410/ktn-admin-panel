# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from src.views.profille import ProfileView
from src.views.root import root_blueprint
from src.views.royalty import RoyaltyView
from src.views.smc_setting import SettingNFTView, SettingStakingView, SettingMarketView

blueprints = [
    root_blueprint
]
pages = [
    # SettingNFTView(name="Nft", category="Blockchain"),
    # SettingStakingView(name="Staking", category="Blockchain"),
    # SettingMarketView(name="Market", category="Blockchain")
    ProfileView(name="Password", category="Account"),
    RoyaltyView(name="Royalty", category="Royalty")

]
