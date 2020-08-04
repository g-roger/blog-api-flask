import copy
import json
import unittest

from app import create_app, db
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
            self.db.session.add(post)
            self.db.session.commit()
            self.post_id = post.id

    def test_get_all_posts(self):
        result = self.client().get('/posts',
                                   content_type='application/json')
        posts = json.loads(result.get_data(as_text=True))

        self.assertEqual(result.status_code, 200)
        self.assertIsNotNone(posts)

    def test_get_post(self):
        result = self.client().get('/post/' + str(self.post_id),
                                   content_type='application/json')

        self.assertEqual(result.status_code, 200)

    def test_register_post(self):
        payload = copy.copy(post_payload)
        result = self.client().post('/post', data=json.dumps(payload),
                                    content_type='application/json')

        courses = json.loads(result.get_data(as_text=True))

        self.assertEqual(result.status_code, 201)
        self.assertIsNotNone(courses['id'])

    def test_update_post(self):
        update_load = {
            "author": "Teste Nome",
            "title": "Exemplo teste modificado",
            "description": "Esse é um exemplo de teste modificado",
            "publication_date": "2020-05-20"
        }

        result = self.client().put('/post/' + str(self.post_id),
                                   data=json.dumps(update_load),
                                   content_type='application/json')

        self.assertEqual(result.status_code, 200)

    def test_delete_post(self):
        result = self.client().delete('/post/' + str(self.post_id),
                                      content_type='application/json')

        self.assertEqual(result.status_code, 200)

    def test_get_invalid_post(self):
        result = self.client().get('/post/49999',
                                   content_type='application/json')

        self.assertEqual(result.status_code, 404)
        self.assertIn('The requested URL was not found on the server. '
                      'If you entered the URL manually please check your '
                      'spelling and try again.', str(result.data))

    def test_update_nonexistent_post(self):
        result = self.client().put('/post/49999',
                                   content_type='application/json',
                                   data=json.dumps(post_payload))

        self.assertEqual(result.status_code, 404)
        self.assertIn('The requested URL was not found on the server. '
                      'If you entered the URL manually please check your '
                      'spelling and try again.', str(result.data))

    def test_delete_nonexistent_post(self):
        result = self.client().delete('/post/49999',
                                      content_type='application/json',
                                      data=json.dumps({}))

        self.assertEqual(result.status_code, 404)
        self.assertIn('The requested URL was not found on the server. '
                      'If you entered the URL manually please check your '
                      'spelling and try again.', str(result.data))

    def tearDown(self):
        with self.app.app_context():
            self.db.session.remove()
