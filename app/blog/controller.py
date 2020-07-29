from flask import jsonify, request
from werkzeug.exceptions import NotFound

from app.blog import blog_blueprint, service
from app.blog.schemas import PostSchema


@blog_blueprint.route('/posts', methods=['GET'])
def get_posts():
    posts = service.get_posts()
    result = PostSchema(many=True).dump(posts)
    return jsonify(result)


@blog_blueprint.route('/post/<int:id>', methods=['GET'])
def get_post(id):
    post = service.get_post(id)

    if post is None:
        raise NotFound

    result = PostSchema().dump(post)
    return jsonify(result)


@blog_blueprint.route('/post', methods=['POST'])
def register_post():
    json_data = request.get_json()

    post = PostSchema().load(json_data)
    result = service.register_post(post)

    return PostSchema().dump(result), 201


@blog_blueprint.route('/post/<int:id>', methods=['PUT'])
def update_post(id):
    json_data = request.get_json()

    post = PostSchema().load(json_data)
    result = service.update_post(id, post)

    if result is None:
        raise NotFound

    return PostSchema().dump(result)


@blog_blueprint.route('/post/<int:id>', methods=['DELETE'])
def delete_post(id):
    result = service.delete_post(id)

    if result is None:
        raise NotFound

    return PostSchema().dump(result)
