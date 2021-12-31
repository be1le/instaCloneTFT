from flask import Blueprint, render_template, request,redirect,url_for
from flask.helpers import url_for
import jwt

from pymongo import MongoClient


client = MongoClient('mongodb+srv://test:sparta@cluster0.0pi7g.mongodb.net/Cluster0?retryWrites=true&w=majority') # 클라이언트 설정시 작성
db = client.dbsparta


SECRET_KEY = 'dev'

mypage = Blueprint("mypage", __name__, url_prefix="/mypage", static_folder="static", template_folder="templates")



@mypage.route("/")
def success():

    token_receive = request.cookies.get('mytoken')
    
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms='HS256')
        
        user_info = db.user.find_one({'id': payload['id']})

        user_pic = db.pic.find_one({'id': payload['id']})

        return render_template('my_page.html', nickname = user_info['nick'], name = user_info['name'], image = user_pic['img']) # db에 저장될 닉네임 값 userinfo

    except jwt.ExpiredSignatureError:
        # 위를 실행했는데 만료시간이 지났으면 에러가 납니다.
        return redirect(url_for('login.home', msg =  '로그인 시간이 만료되었습니다.'))
    except jwt.exceptions.DecodeError:
        return redirect(url_for('login.home', msg = '로그인 정보가 존재하지 않습니다.'))








