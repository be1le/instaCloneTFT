from flask import render_template, request, jsonify
from flask.blueprints import Blueprint

from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.0pi7g.mongodb.net/Cluster0?retryWrites=true&w=majority')  # 클라이언트 설정시 작성
db = client.dbsparta

# 로그인 기능
import hashlib
import datetime
import jwt

SECRET_KEY = 'dev'



sign_up = Blueprint("sign_up", __name__ , url_prefix="/sign", static_folder="static", template_folder="templates")


@sign_up.route("/")
def sign():
    return render_template("sign_up.html")


@sign_up.route('/check_dup', methods=['POST'])
def check_dup():
    username_receive = request.form['userid_give']

    exists = bool(db.users.find_one({"id": username_receive}))
    
    return jsonify({'result': 'success', 'exists': exists})


@sign_up.route("/register", methods=['POST'])
def register():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    name_receive = request.form['name_give']
    nickname_receive = request.form['nickname_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    db.user.insert_one({'id': id_receive, 'pw': pw_hash, 'name': name_receive, 'nick': nickname_receive})
    

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


@sign_up.route("/api/nickname", methods=['GET'])
def api_valid():
    token_receive = request.cookies.get('mytoken')
    print(token_receive)

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




# id , pw  조건 수정하기

