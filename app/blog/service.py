from app import db
from app.blog.models import Post


def get_posts():
    posts = Post.query.all()
    return posts


def get_post(id):
    post = Post.query.get(id)
    return post


def register_post(post):
    db.session.add(post)
    db.session.commit()
    return post


def update_post(id, updated_post):
    database_post = Post.query.get(id)

    if not database_post:
        return None

    editable_attributes = [
        'author', 'title', 'description', 'publication_date'
    ]

    for attribute in editable_attributes:
        setattr(database_post,
                attribute,
                updated_post.__dict__[attribute])

    db.session.add(database_post)
    db.session.commit()
    return database_post


def delete_post(id):
    database_post = Post.query.get(id)
    if not database_post:
        return None

    db.session.delete(database_post)
    db.session.commit()
    return database_post
