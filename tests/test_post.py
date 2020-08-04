import json
import unittest

from app import create_app, db
from app.blog.models import Post
from app.blog.schemas import PostSchema

post_payload = {
    "author": "Gabriel Roger",
    "title": "Exemplo teste",
    "description": "Esse é um exemplo de teste",
    "publication_date": "2020-05-20"
}


class PostTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client
        self.db = db

        post = PostSchema().load(post_payload)

        with self.app.app_context():
            self.db.create_all()

    def tearDown(self):
        with self.app.app_context():
            self.db.session.remove()
            self.db.drop_all()
