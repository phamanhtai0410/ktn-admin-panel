# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from src.views.root import root_blueprint
from src.views.smc_setting import SettingNFTView, SettingStakingView, SettingMarketView

blueprints = [
    root_blueprint
]
pages = [
    SettingNFTView(name="Nft", category="Blockchain"),
    SettingStakingView(name="Staking", category="Blockchain"),
    SettingMarketView(name="Market", category="Blockchain")
]
