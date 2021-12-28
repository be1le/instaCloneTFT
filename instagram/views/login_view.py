from flask import Blueprint, render_template

login = Blueprint("login", __name__, url_prefix="/" ,  static_folder="static", template_folder="templates")


@login.route("/")
def home():
    return render_template("login.html")

@login.route("/success")
def success():
    return render_template("main.html")

@login.route("/fail")
def fail():
    return "로그인 실패"

@login.route("/sign_up")
def sign_up():
    return "회원가입 페이지"