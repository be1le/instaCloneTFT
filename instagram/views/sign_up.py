from os import stat
from flask import Flask, render_template
from flask.blueprints import Blueprint

sign_up = Blueprint("sign_up", __name__ , url_prefix="/sign", static_folder="static", template_folder="templates")


@sign_up.route("/")
def sign():
    return render_template("sign_up.html")

