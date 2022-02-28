from sqlalchemy import null
from app import db



class TechStack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_name = db.Column(db.String(30))
    name = db.Column(db.String(30), unique=True,nullable=False)
    description = db.Column(db.String(240),nullable=False)
    def __repr__(self):
        return f'<{self.name}>'

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_name = db.Column(db.String(30))
    name = db.Column(db.String(10),unique=True, nullable=False)
    description = db.Column(db.String(150), nullable=False)
    github = db.Column(db.String(120), nullable=False)
    tag_urls = db.Column(db.String(120), nullable=True)
    def __repr__(self):
        return f'<Project {self.name}>'