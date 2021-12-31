from flask import Flask, render_template, request, redirect, url_for, jsonify,Blueprint
from datetime import datetime
from pymongo import MongoClient
import jwt
import hashlib

app = Flask(__name__)


client = MongoClient('mongodb+srv://test:sparta@cluster0.0pi7g.mongodb.net/Cluster0?retryWrites=true&w=majority') # 클라이언트 설정시 작성
db = client.dbsparta

SECRET_KEY = 'dev'

change_pw = Blueprint("change_pw", __name__, url_prefix="/change_pw", static_folder="static", template_folder="templates")



@change_pw.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms='HS256')
        
        user_info = db.user.find_one({'id': payload['id']})

        return render_template('change_pw.html', nickname = user_info['nick'], name = user_info['name']) # 닉네임,네임 님 비밀 번호 변경 하시겠습니까?

    except jwt.ExpiredSignatureError:
        # 위를 실행했는데 만료시간이 지났으면 에러가 납니다.
        return redirect(url_for('login.home', msg =  '로그인 시간이 만료되었습니다.'))
    except jwt.exceptions.DecodeError:
        return redirect(url_for('login.home', msg = '로그인 정보가 존재하지 않습니다.'))

@change_pw.route('/change_pw')
def change():
    ############## 빈칸 불가능 절대 불가능
    password_receive = request.form['pw_give']

    token_receive = request.cookies.get('mytoken')
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms='HS256')


    
    user = db.user.find_one({'id': payload['id']})
    user_id = user['id']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    

    db.user.update_one({'id':user_id},{'$set':{'pw': pw_hash}})
    
    
