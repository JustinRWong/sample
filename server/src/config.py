import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'secret'
    USE_FIREBASE_STATIC_ASSET_SOURCE = False


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = 'secret'
    USE_FIREBASE_STATIC_ASSET_SOURCE=True

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SECRET_KEY = 'secret'


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SECRET_KEY = 'secret'
    USE_FIREBASE_STATIC_ASSET_SOURCE=False


class TestingConfig(Config):
    TESTING = True
