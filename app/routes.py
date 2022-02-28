from app import app
from flask import render_template, request, redirect, url_for
from flask_login import login_required
from werkzeug.utils import secure_filename
import os
from app.models import TechStack, Project
#Route Home / or /home
@app.route('/home')
@app.route('/')
def home():
    techstack = TechStack.query.all()
    return render_template('index.html',techstack=techstack)


@app.route('/image_upload', methods=['GET','POST'])
@login_required
def image_upload():
    if request.method=='POST':
        f=request.files['img']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        return redirect(url_for('image_upload',status='Success'))
    return render_template('image_upload.html')