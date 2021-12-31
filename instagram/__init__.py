from flask import Flask, render_template, request, jsonify


from pymongo import MongoClient



def create_app():
    app = Flask(__name__)


    from.views import login_view, sign_up,mypage,profile_change_view,change_pw_view
    from.main import main

    app.register_blueprint(login_view.login)
    app.register_blueprint(main)
    app.register_blueprint(sign_up.sign_up)
    app.register_blueprint(mypage.mypage)
    app.register_blueprint(profile_change_view.profile)
    app.register_blueprint(change_pw_view.change_pw)
    return app
    
    ''' 
    로그인 페이지
    회원가입 페이지
    게시물 페이지
    나의 게시물 페이지
    글작성 페이지
    '''