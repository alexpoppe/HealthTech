from flask import Blueprint, request, render_template


api = Blueprint("api", __name__, template_folder='templates', static_folder='static', static_url_path='api/static')


@api.route("/", methods=["GET"])
def home():
    return render_template("index.html")

