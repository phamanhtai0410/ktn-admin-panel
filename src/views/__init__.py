# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from src.views.root import root_blueprint
from src.views.smc_setting import SettingSmcView

blueprints = [
    root_blueprint
]
pages = [
    SettingSmcView(name="Setting", category="Blockchain", endpoint="blockchain")
]
