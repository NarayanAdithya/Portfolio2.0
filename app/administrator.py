from flask_admin.contrib.sqla import ModelView
from app.models import TechStack
from app import admin, db, login
from flask_login import current_user
from flask import request, redirect, url_for
class PortfolioModelView(ModelView):
    
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('login'))
    
admin.add_view(PortfolioModelView(TechStack,db.session))