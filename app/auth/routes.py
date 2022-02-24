from app import db
from flask_login import current_user,logout_user
from datetime import datetime
from flask import request,redirect,url_for,render_template
from . import auth


@auth.route('/logout')
def logout():
    current_user.last_seen=datetime.utcnow()
    db.session.commit()
    logout_user()
    return redirect(url_for('home.index'))



@auth.route('/adithyalogin',methods=['GET','POST'])
def loginUser():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return render_template('login_adithya.html')




