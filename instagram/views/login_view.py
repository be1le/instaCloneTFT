from flask import Blueprint, render_template ,jsonify, request, session, redirect, url_for
import datetime
import hashlib
import jwt

from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.0pi7g.mongodb.net/Cluster0?retryWrites=true&w=majority') # 클라이언트 설정시 작성
db = client.dbsparta


SECRET_KEY = 'dev'


login = Blueprint("login", __name__, url_prefix="/" ,  static_folder="static", template_folder="templates")


@login.route("/")
def home():
    msg = request.args.get("msg")
    return render_template("index.html" , msg = msg)

@login.route("/api/login", methods=["POST"])
def api_login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    result = db.user.find_one({'id': id_receive, 'pw': pw_hash})
    
    if result is not None:
        payload = {
            'id' : id_receive, 
            'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds=60 * 60 )  
            }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return jsonify({'result': 'success', 'token': token})
    
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지않습니다'})


@login.route("/api/nickname", methods=['GET'])
def api_valid():
    token_receive = request.cookies.get('mytoken')


    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms='HS256')
        print(payload)

        userinfo = db.user.find_one({'id': payload['id']} , {'_id': 0})
        return jsonify({'result': 'success', 'nickname': userinfo['nick']}) # db에 저장될 닉네임 값 userinfo

    except jwt.ExpiredSignatureError:
        # 위를 실행했는데 만료시간이 지났으면 에러가 납니다.
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})




