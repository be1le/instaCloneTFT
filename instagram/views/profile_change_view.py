from flask import Flask, render_template, request, redirect, url_for, jsonify,Blueprint
from datetime import datetime
from pymongo import MongoClient
import jwt
import os

app = Flask(__name__)


client = MongoClient('mongodb+srv://test:sparta@cluster0.0pi7g.mongodb.net/Cluster0?retryWrites=true&w=majority') # 클라이언트 설정시 작성
db = client.dbsparta

SECRET_KEY = 'dev'

profile = Blueprint("profile", __name__, url_prefix="/profile", static_folder="static", template_folder="templates")



@profile.route("/")
def success():

    token_receive = request.cookies.get('mytoken')
    
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms='HS256')
        
        user_info = db.user.find_one({'id': payload['id']})
        
        user_pic = db.pic.find_one({'id': payload['id']})

        if user_pic != None:
            return render_template('profile.html', nickname = user_info['nick'], name = user_info['name'], image = user_pic['img']) 
        else :
            return render_template('profile.html', nickname = user_info['nick'], name = user_info['name']) # 프로필 사진이 없을때.

    except jwt.ExpiredSignatureError:
        # 위를 실행했는데 만료시간이 지났으면 에러가 납니다.
        return redirect(url_for('login.home', msg =  '로그인 시간이 만료되었습니다.'))
    except jwt.exceptions.DecodeError:
        return redirect(url_for('login.home', msg = '로그인 정보가 존재하지 않습니다.'))



#닉네임 변경 , 프로필 사진 변경 (기존 파일 삭제 및 추가)

@profile.route('/fileupload', methods=['POST'])
def file_upload():
    ##### file_give 가  none 일 경우
    ########### files 값 여부 확인하고 ...?
    try:
        nick_receive = request.form['nick_give'] # input 닉네임
        file = request.files['file_give'] #upload 파일
        
        token_receive = request.cookies.get('mytoken')
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms='HS256')
        user = db.user.find_one({'id': payload['id']})
        user_id = user['id']

        
        extension = file.filename.split('.')[-1]


        today = datetime.now()
        mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
        filename = f'{user_id}-{mytime}'

        profile = db.pic.find_one({'id': user_id})
        
        if profile != None :
            profile_pic = profile['img']
            os.remove( f'instagram/static/images/profile_images/{profile_pic}' )
        
        db.pic.delete_one({ 'id': user_id })

        # 파일 저장 경로 설정 (파일은 db가 아니라, 서버 컴퓨터 자체에 저장됨)
        save_to = f'instagram/static/images/profile_images/{filename}.{extension}'
        # 파일 저장!
        file.save(save_to)
        
        
        doc = {'id': user_id, 'img':f'{filename}.{extension}'}
        db.pic.insert_one(doc)
        
        if nick_receive != '' :
            db.user.update_one({'id': user_id },{'$set':{'nick': nick_receive }})

        return jsonify({'result':'success'})
    except:
        nick_receive = request.form['nick_give'] # input 닉네임
        
        token_receive = request.cookies.get('mytoken')
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms='HS256')
        user = db.user.find_one({'id': payload['id']})
        user_id = user['id']

        if nick_receive != '' :
            db.user.update_one({'id': user_id },{'$set':{'nick': nick_receive }})

        return jsonify({'result':'success'})