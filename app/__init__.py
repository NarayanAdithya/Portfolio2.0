#Import of necessary utility functions
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_admin import Admin
from dotenv import load_dotenv
import os


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

#Login Configurations
login = LoginManager(app)
login.login_view='auth.loginUser'

#Blueprine Registration
from app.auth import auth
app.register_blueprint(auth,url_prefix='/auth')
print(app.config['UPLOAD_FOLDER'])
from app import routes, models


