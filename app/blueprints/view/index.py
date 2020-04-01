from flask.views import MethodView
from flask import render_template


class Index(MethodView):

    name = "index"
    path = "/"

    def get(self):
        return render_template("view/index.html")
