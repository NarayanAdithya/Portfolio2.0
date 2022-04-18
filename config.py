from distutils.debug import DEBUG
import os

from sqlalchemy import true
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    ENVIRONMENT = os.environ.get('environment')
    SECRET_KEY = os.environ.get('SECRET_KEY','sjskfdojg&*&(9')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
    FLASK_ADMIN_SWATCH='cerulean'
    PROJECT_UPLOAD_FOLDER = os.environ.get('PROJECT_UPLOAD_FOLDER')
    ADI_BOT_URL = os.environ.get('ADI_BOT_ENDPOINT')
    
class Development(Config):
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    DEBUG = True
    MONGO_URI = os.environ.get("MONGO_URI")
class Production(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    DEBUG=False
    MONGO_URI = os.environ.get("MONGO_URI")
    