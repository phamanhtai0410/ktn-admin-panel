from markupsafe import Markup
from flask_admin import BaseView, expose
from pydash import get

from src.abis import nft_abi, staking_abi, creator_abi
from src.config import Config


class SettingNFTView(BaseView):

    @expose('/')
    def index(self):
        _functions = ['setMinterRole', 'setMaxTokensInOneMint',
                      'setMaxTokensInOneUing', 'setWhiteList',
                      'switchFreeTransferMode', 'addNewNftType',
                      'upgradeExistingNftType', 'grantRole']

        return self.render("pages/smc_setting.html",
                           address=Config.NFT_ADDRESS,
                           abis=[
                               abi for abi in nft_abi if get(abi, 'name') in _functions
                           ])


class SettingStakingView(BaseView):

    @expose('/')
    def index(self):
        _functions = ['setRewardsPerHour', 'addNewCollection',
                      'removeCollection', 'grantRole']

        return self.render("pages/smc_setting.html",
                           address=Config.STAKING_ADDRESS,
                           abis=[
                               abi for abi in staking_abi if get(abi, 'name') in _functions
                           ])


class SettingMarketView(BaseView):

    @expose('/')
    def index(self):
        _functions = ['setPayToken', 'updatePrice',
                      'grantRole', 'nftPrice']

        return self.render("pages/smc_setting.html",
                           address=Config.CREATOR_ADDRESS,
                           abis=[
                               abi for abi in creator_abi if get(abi, 'name') in _functions
                           ])
