#Import of necessary utility functions
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_admin import Admin
from dotenv import load_dotenv
from flask_socketio import SocketIO
import os
from pymongo import MongoClient


socketio=SocketIO()
#Loading Env's
load_dotenv()

#Importing Config
import config

#App Declaration and configuration
app = Flask(__name__)
print(os.environ.get('environment'))
if os.environ.get('environment')=='Development':
    app.config.from_object(config.Development)
elif os.environ.get('environment')=='Production':
    app.config.from_object(config.Production)

#Database Configuration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#DataBase Mongo
db_mongo = MongoClient(app.config.get('CONNECTION_URL'))
db_mongo=db_mongo['Adi_Bot']
db_m = db_mongo['Chats']
#Login Configurations
login = LoginManager(app)
login.login_view='auth.loginUser'

#Flask Admin Configurations
admin = Admin(app, name='Portfolio', template_mode='bootstrap3')


#SocketIO Init
socketio.init_app(app, cors_allowed_origins="*")

#Blueprine Registration
from app.auth import auth
from app.bot import bot
app.register_blueprint(auth,url_prefix='/auth')
app.register_blueprint(bot,url_prefix='/bot')
from app import routes, models, administrator

