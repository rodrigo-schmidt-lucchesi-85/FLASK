import os
basedir = os.path.abspath(os.path.dirname(__file__)) # Root path


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "secret-key"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db') # Inheriting root path for app.db creation
    SQLALCHEMY_TRACK_MODIFICATIONS = False # SQLALCHEMY_TRACK_MODIFICATIONS allows you to disable the modification tracking system.


class ProductioConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True