from flask import Blueprint, render_template, request,redirect,url_for,jsonify
import jwt
from datetime import datetime
import time


from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.0pi7g.mongodb.net/Cluster0?retryWrites=true&w=majority') 
db = client.dbsparta


SECRET_KEY = 'dev'

### 블루프린트 지정 ###
main = Blueprint("main", __name__, url_prefix="/main", static_folder="static", template_folder="templates")


#### 토큰 값으로 유저 정보를 불러와서 프로필사진 이미지 이름을 feed_page로 보내준다 #####


@main.route("/")
def success():

    token_receive = request.cookies.get('mytoken')
    
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms='HS256')
        
        user_info = db.user.find_one({'id': payload['id']})

        user_pic = db.pic.find_one({'id': payload['id']})

        if user_pic != None:
            return render_template('feed_page.html', nickname = user_info['nick'], name = user_info['name'], image = user_pic['img']) 
        else :
            return render_template('feed_page.html', nickname = user_info['nick'], name = user_info['name']) # 프로필 사진이 없을때.
    except jwt.ExpiredSignatureError:
        # 위를 실행했는데 만료시간이 지났으면 에러가 납니다.
        return redirect(url_for('login.home', msg =  '로그인 시간이 만료되었습니다.'))
    except jwt.exceptions.DecodeError:
        return redirect(url_for('login.home', msg = '로그인 정보가 존재하지 않습니다.'))


######## 글 작성 부분  #########

@main.route("/addpost", methods=['POST'])
def add():

    text_receive = request.form['text_give'] # input 닉네임
    file = request.files['file_give']

    # 토큰값을 가져와서 유저 정보를 DB에서 불러 온다 
    token_receive = request.cookies.get('mytoken')

    payload = jwt.decode(token_receive, SECRET_KEY, algorithms='HS256')
    
    # 여기는 유저 DB
    user_info = db.user.find_one({'id': payload['id']})

    # 여기는 프로필 사진 DB
    user_profile = db.pic.find_one({'id': payload['id']})

    #postid 를 db의 길이 + 1을하여 지정해줌
    postid = len(db.feed) + 1

    # 유저의 id , 닉네임 , 프로필 사진을 불러온다.
    user_id = user_info['id']
    user_nick = user_info['nick']
    user_profile = user_profile['img']
    
    like = 0
    save = 0

    # 사진 의 확장자 명만 따옴
    extension = file.filename.split('.')[-1] 

    ############# 시간 저장 변수 ######################
    today = datetime.now()
    millis = int(round(time.time() * 1000))
    post_time = today.strftime('%Y-%m-%d-%H-%M-%S')

    #파일이름 저-장
    filename = f'{user_id}-{post_time}'

    save_to = f'instagram/static/images/feed_images/{filename}.{extension}'
    # 파일 저장!
    file.save(save_to)

    # feed DB에 피드 정보를 저장한다.
    doc = {'id': user_id ,'photo': f'{filename}.{extension}', 'like': like , 'save': save, 'text': text_receive, 'postid': postid, 'date': millis, 'nick': user_nick, 'profile': user_profile}

    db.feed.insert_one(doc)




#불러 오기#
@main.route("/loadpost", methods=["GET"])
def movie_get():
    
    all_feeds = list(db.feed.find({},{'_id':False}).sort("date",-1))
    all_comment = list(db.comment.find({},{'_id':False}).sort("date",-1))
    return jsonify({'feeds': all_feeds}, {'comments': all_comment})











