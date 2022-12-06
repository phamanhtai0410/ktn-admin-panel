# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
import sys

from eth_account import Account
from pymongo import MongoClient
from web3 import Web3, HTTPProvider
from web3.middleware import construct_sign_and_send_raw_middleware

sys.path.append('.')

from src.abis import factory_abi

rpc = ''
factory_address = ''
private_key = ''
MONGO_URI = ''


_web3 = Web3(HTTPProvider(rpc))
account = Account.from_key(private_key)
_web3.middleware_onion.add(
    construct_sign_and_send_raw_middleware(account)
)
_web3.eth.default_account = account.address
_factory = _web3.eth.contract(factory_address, abi=factory_abi)

db = MongoClient(MONGO_URI, connect=False)['katana-dapp']

collectionModel = db['collection']
rarityModel = db['rarities']
meshModel = db['meshes']
meshMaterialModel = db['mesh_materials']



