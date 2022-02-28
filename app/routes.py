from app import app
from flask import render_template, request, redirect, url_for, send_from_directory
from flask_login import login_required
from werkzeug.utils import secure_filename
import os
from app.models import TechStack, Project
import json
#Route Home / or /home
@app.route('/home')
@app.route('/')
def home():
    techstack = TechStack.query.all()
    projects = Project.query.all()
    tags=[]
    for i in projects:
        tags.append(json.loads(i.tag_urls))
    return render_template('index.html',techstack=techstack,projects=projects,p_tags=tags)


@app.route('/image_upload', methods=['GET','POST'])
@login_required
def image_upload():
    if request.method=='POST':
        f=request.files['img']
        if request.form['folder']=='tech_stack':
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        else:
            f.save(os.path.join(app.config['PROJECT_UPLOAD_FOLDER'], secure_filename(f.filename)))
        return redirect(url_for('image_upload',status='Success'))
    return render_template('image_upload.html')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(app.static_folder,'sitemap.xml')

@app.route('/robots.txt')
def sitemap():
    return send_from_directory(app.static_folder,'robots.txt')