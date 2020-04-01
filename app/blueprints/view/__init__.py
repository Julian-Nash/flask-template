from flask import Blueprint

from .index import Index

routes = (Index,)

view = Blueprint("view", __name__, template_folder="view")

for route in routes:
    view.add_url_rule(route.path, view_func=route.as_view(route.name))
