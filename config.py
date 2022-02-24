import os

class Config():
    ENVIRONMENT = os.environ.get('environment')


class Development(Config):
    DATABASE_URI = SQLALCHEMY_DATABASE_URI = 'sqlite:///' + 'app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class Production(Config):
    DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS=False