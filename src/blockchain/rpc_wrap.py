# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
import traceback

import sentry_sdk
from eth_account import Account
from web3 import Web3
from web3.middleware import construct_sign_and_send_raw_middleware, geth_poa_middleware

from src.abis import creator_abi
from src.config import Config


class RPCWrap(Web3):

    def __init__(self, private_key, *args, **kwargs):
        super(RPCWrap, self).__init__(*args, **kwargs)
        self.my_account = Account.from_key(private_key)
        self.middleware_onion.add(
            construct_sign_and_send_raw_middleware(self.my_account)
        )
        self.middleware_onion.inject(geth_poa_middleware, layer=0)

        self.eth.default_account = self.my_account.address

    @property
    def smc_creator(self):
        try:
            return self.eth.contract(self.toChecksumAddress(Config.CREATOR_ADDRESS), abi=creator_abi)
        except:
            traceback.print_exc()
            sentry_sdk.capture_exception()
        return None
