from flask import Flask



def create_app():
    app = Flask(__name__)

    from.views import login_view, profile_change_view, change_pw_view, main_view, mypage_view, sign_up_view
    

    app.register_blueprint(login_view.login)
    app.register_blueprint(main_view.main)
    app.register_blueprint(sign_up_view.sign_up)
    app.register_blueprint(mypage_view.mypage)
    app.register_blueprint(profile_change_view.profile)
    app.register_blueprint(change_pw_view.change_pw)

    return app
    
    ''' 
    로그인 페이지
    회원가입 페이지
    게시물 페이지
    마이 페이지
    비밀번호 변경 페이지
    프로필 변경 페이지
    글작성 페이지
    '''