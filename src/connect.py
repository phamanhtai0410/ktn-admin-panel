# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
import os
from web3 import HTTPProvider

from src.blockchain.rpc_wrap import RPCWrap
from src.config import Config

with open(os.getenv('PRIVATE_PATH')) as f:
    _private = f.read()
    f.close()

bsc = RPCWrap(_private, HTTPProvider(Config.BSC_RPC))
