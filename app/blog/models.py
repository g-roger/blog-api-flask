from datetime import datetime

from app import db


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(128))
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    publication_date = db.Column(db.DateTime, default=datetime.utcnow)
