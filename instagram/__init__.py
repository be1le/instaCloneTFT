from flask import Flask , render_template, request, jsonify
# from flask.helpers import url_for


from pymongo import MongoClient


def create_app():
    app = Flask(__name__)

    from.views import login_view, sign_up
    from.main import main

    app.register_blueprint(login_view.login)
    app.register_blueprint(main)
    app.register_blueprint(sign_up.sign_up)

    return app
    
    ''' 
    로그인 페이지
    회원가입 페이지
    게시물 페이지
    나의 게시물 페이지
    '''