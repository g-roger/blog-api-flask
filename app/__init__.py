from flask import Flask
from config import app_config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate(compare_type=True)


def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)

    from app.blog import blog_blueprint
    app.register_blueprint(blog_blueprint)

    return app
