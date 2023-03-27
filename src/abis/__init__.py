# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
import json

staking_abi = None
with open("src/abis/staking.json") as f:
    staking_abi = json.loads(f.read())
    f.close()

nft_abi = None
with open("src/abis/NFT.json") as f:
    nft_abi = json.loads(f.read())
    f.close()

creator_abi = None
with open("src/abis/CREATER.json") as f:
    creator_abi = json.loads(f.read())
    f.close()

factory_abi = None
with open("src/abis/FACTORY.json") as f:
    factory_abi = json.loads(f.read())
    f.close()

box_creator_abi = None
with open("src/abis/BOX_CREATOR.json") as f:
    box_creator_abi = json.loads(f.read())
    f.close()

box_factory_abi = None
with open("src/abis/BOX_FACTORY.json") as f:
    box_factory_abi = json.loads(f.read())
    f.close()
royalty_controller_abi = None

with open("src/abis/RoyaltyController.json") as f:
    royalty_controller_abi = json.loads(f.read())
    f.close()
