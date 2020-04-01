from flask import Flask

from app.config import get_config
from app.blueprints.view import view


def create_app(config):
    """ Application factory """

    app = Flask(__name__)

    config = get_config(config)
    app.config.from_object(config)

    app.logger.info(f"{config.__name__} loaded")

    app.register_blueprint(view)

    return app
