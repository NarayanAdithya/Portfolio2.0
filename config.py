import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    ENVIRONMENT = os.environ.get('environment')
    SECRET_KEY = os.environ.get('SECRET_KEY','sjskfdojg&*&(9')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
    FLASK_ADMIN_SWATCH='cerulean'
class Development(Config):
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class Production(Config):
    DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS=False