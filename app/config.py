import os
from datetime import timedelta
from typing import Type


class Config(object):
    SECRET_KEY = os.urandom(64)
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"


class ProductionConfig(Config):
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=60)


class DevelopmentConfig(Config):
    SECRET_KEY = "secret"
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    SECRET_KEY = "secret"
    SESSION_COOKIE_SECURE = False


def get_config(config: str) -> Type[Config]:
    """ Returns a Config class, defaults to ProductionConfig

    Args:
        config (str): The name of the config to return (production|development|testing)
    Returns:
        A Config object
    """

    config_map = {
        "production": ProductionConfig,
        "development": DevelopmentConfig,
        "testing": TestingConfig
    }

    return config_map.get(config, ProductionConfig)
