# Creating a config file to be used across the Flask app.
# The secret key is a way to keep secret cookies and information during user session
class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "secret-key"

class ProductioConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True