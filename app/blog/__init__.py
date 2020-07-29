from flask import Blueprint
from app.blog.models import Post

blog_blueprint = Blueprint('blog', __name__)

from app.blog import controller
