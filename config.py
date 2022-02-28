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
    
class Development(Config):
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    DEBUG = True

class Production(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    DEBUG=False