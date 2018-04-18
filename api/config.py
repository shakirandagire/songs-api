import os

class BaseConfig(object):
    TESTING = False
    DEBUG = False
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI ='postgresql://@localhost/songs_db'
    SQLALCHEMY_TRACK_MODIFICATION = False

class Development(BaseConfig):
    DEBUG = True

class Testing(BaseConfig):
    TESTING = False
    SQLALCHEMY_DATABASE_URI ='postgresql://@localhost/test_songs_db'

app_config ={
    'development': Development,
    'testing': Testing
}

