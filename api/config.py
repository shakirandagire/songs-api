import os

class BaseConfig(object):
    TESTING = False
    DEBUG = False
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI =os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATION = False

class Development(BaseConfig):
    DEBUG = True

class Testing(BaseConfig):
    TESTING = False
    SQLALCHEMY_DATABASE_URI =os.environ.get('TEST_DATABASE_URL')

app_config ={
    'development': Development,
    'testing': Testing
}

