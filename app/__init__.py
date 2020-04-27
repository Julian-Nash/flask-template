from typing import Type

from flask import Flask

from app.config import get_config, Config
from app.blueprints.view import view


def create_app(env: str) -> Flask:
    """ Application factory """

    app = Flask(__name__)
    conf: Type[Config] = get_config(env)

    app.config.from_object(conf)
    app.register_blueprint(view)

    return app
