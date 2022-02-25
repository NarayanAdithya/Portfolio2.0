from app import app
from flask import render_template, request
from flask_login import login_required
from werkzeug.utils import secure_filename
import os
#Route Home / or /home
@app.route('/home')
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/image_upload', methods=['GET','POST'])
@login_required
def image_upload():
    if request.method=='POST':
        f=request.files['img']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        return 'file uploaded successfully'
    return render_template('image_upload.html')