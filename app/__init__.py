from flask import Flask

from app.config import get_config
from app.blueprints.view import view


def create_app(env: str):
    """ Application factory """

    app = Flask(__name__)

    config = get_config(env)
    app.config.from_object(config)

    app.logger.info(f"{config.__name__} loaded")

    app.register_blueprint(view)

    return app
