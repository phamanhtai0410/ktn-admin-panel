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
