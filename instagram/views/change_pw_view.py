from flask import Flask, render_template, request, redirect, url_for, jsonify,Blueprint
from datetime import datetime
from pymongo import MongoClient
import jwt
import hashlib
import re

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

        user_pic = db.pic.find_one({'id': payload['id']})

        if user_pic != None:
            return render_template('change_pw.html', nickname = user_info['nick'], name = user_info['name'], image = user_pic['img'])
        else :
            return render_template('change_pw.html', nickname = user_info['nick'], name = user_info['name']) # 프로필 사진이 없을때.

    except jwt.ExpiredSignatureError:
        # 위를 실행했는데 만료시간이 지났으면 에러가 납니다.
        return redirect(url_for('login.home', msg =  '로그인 시간이 만료되었습니다.'))
    except jwt.exceptions.DecodeError:
        return redirect(url_for('login.home', msg = '로그인 정보가 존재하지 않습니다.'))


@change_pw.route('/go', methods=['POST'])
def change():
    ############## 빈칸 불가능 절대 불가능
    password_receive = request.form['old_password_give']
    new_receive = request.form['new_password_give']
    new_2_receive = request.form['check_new_password_give']

    token_receive = request.cookies.get('mytoken')
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms='HS256')

    old = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    user = db.user.find_one({'id': payload['id']})
    
    user_id = user['id']
    user_pw = user['pw']

    
    #re ( 정규식 연산) 모듈을 사용하여 파이썬에서 비밀번호 조건 검사 
    #.search( pattern, string) 
    # string 을 검사하여 pattern 에 들어가는 정규식과 일치하면 일치 객체 반환 (일치객체는 항상 True를 가짐),
    # 일치하지 않으면 None 을 반환 합니다 
    # 이것을 이용하여 정규표현식을 파이썬에서 구현하여 변경될 새비밀번호가 유효한지를 검사하게 함
    if old == user_pw :
        if new_receive == new_2_receive:
            if len(new_receive) < 8:
                return jsonify({'result': 'fail','msg':'새 비밀번호가 8자 이하입니다.'})
            elif re.search('[0-9]',new_receive) is None:
                return jsonify({'result': 'fail','msg':'숫자를 포함해주세요.'})
            elif re.search('[a-z]',new_receive) is None: 
                return jsonify({'result': 'fail','msg':'영문 문자를 포함해주세요.'})
            else:
                pw_hash = hashlib.sha256(new_receive.encode('utf-8')).hexdigest()
            
                db.user.update_one({'id':user_id},{'$set':{'pw': pw_hash}})
                return jsonify({'result': 'success','msg':'비밀번호가 변경 되었습니다.'})
        else:
            return jsonify({'result': 'fail','msg':'새 비밀번호가 서로 맞지않습니다.'})
    else:
        return jsonify({'result': 'fail', 'msg':'비밀번호가 틀렸습니다.'})
