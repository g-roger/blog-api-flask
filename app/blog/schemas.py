from marshmallow import Schema, fields, post_load

from app.blog.models import Post


class PostSchema(Schema):
    id = fields.Integer(required=False, dump_only=True)
    author = fields.String(required=True)
    title = fields.String(required=True)
    description = fields.String(required=True)
    publication_date = fields.DateTime()

    @post_load
    def make_post(self, data, **kwargs):
        return Post(**data)
