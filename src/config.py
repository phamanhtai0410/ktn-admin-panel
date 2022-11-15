# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    PROJECT_NAME = 'Admin panel'
    TEMPLATE_MODE = 'bootstrap4'
    MONGO_URI = os.getenv('MONGO_URI')
    BSC_SCAN = os.getenv('BSC_SCAN')
    ETH_SCAN = os.getenv('ETH_SCAN')

    SENTRY_DSN = os.getenv('SENTRY_DSN')
    SECRET_KEY = 'zTVDE1WG9Tg4BbxNi21A'
    SECURITY_PASSWORD_SALT = 'bcrypt'
    MONGODB_SETTINGS = [
        {
            'alias': 'default',
            'host': MONGO_URI
        }
    ]
    ASSETS_ROOT = '/static/assets'
    # security
    SECURITY_USER_IDENTITY_ATTRIBUTES = ('email')
    ADMIN_ROOT = 'root@katana.com'
    NFT_ADDRESS = os.getenv('NFT_ADDRESS')
    STAKING_ADDRESS = os.getenv('STAKING_ADDRESS')
    CREATOR_ADDRESS = os.getenv('CREATOR_ADDRESS')
    BSC_RPC = os.getenv('BSC_RPC')
    NFT_FACTORY_ADDRESS = os.getenv('NFT_FACTORY_ADDRESS')
    # S3
    AWS_KEY = os.getenv('AWS_KEY')
    AWS_SECRET = os.getenv('AWS_SECRET')
    BUCKET_NAME = os.getenv('BUCKET_NAME')
    S3_HOST = os.getenv('S3_HOST')
    S3_STATIC = os.getenv('S3_STATIC')
    pass
