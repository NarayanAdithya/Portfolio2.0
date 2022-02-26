from enum import unique
from app import db, login
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    role=db.Column(db.String(20),default='Admin')
    password_hash_key1=db.Column(db.String(120))
    password_hash_key2=db.Column(db.String(120))
    password_hash_key3=db.Column(db.String(120))
    def set_password(self,key1,key2,key3):
        self.password_hash_key1=generate_password_hash(key1)
        self.password_hash_key2=generate_password_hash(key2)
        self.password_hash_key3=generate_password_hash(key3)
    def check_password(self,k1,k2,k3):
        return check_password_hash(self.password_hash_key1,k1) and check_password_hash(self.password_hash_key2,k2) and check_password_hash(self.password_hash_key3,k3)



