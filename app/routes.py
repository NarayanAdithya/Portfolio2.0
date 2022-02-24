from app import app
from flask import render_template



#Route Home / or /home
@app.route('/home')
@app.route('/')
def home():
    return render_template('index.html')


