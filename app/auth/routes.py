from app import db
from flask_login import current_user,logout_user
from datetime import datetime
from flask import request,redirect,url_for,render_template
from flask_login import login_user
from . import auth
from app.auth.models import User


@auth.route('/logout')
def logout():
    current_user.last_seen=datetime.utcnow()
    db.session.commit()
    logout_user()
    return redirect(url_for('home'))

@auth.route('/invalid')
def invalid():
    return render_template('invalid.html')

@auth.route('/adithyalogin',methods=['GET','POST'])
def loginUser():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method=='POST':
        k1, k2, k3 = request.form['k1'], request.form['k2'], request.form['k3']
        u=User.query.get(1)
        if u.check_password(k1,k2,k3):
            login_user(u)
            return redirect(url_for('home'))
        else:
            return redirect(url_for('auth.invalid'))
    return render_template('login_adithya.html')




