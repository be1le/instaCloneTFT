from flask import Blueprint, render_template, request,redirect,url_for,jsonify
import jwt
from datetime import datetime
import time
import math

from pymongo import MongoClient
from pymongo.common import RETRY_WRITES
from werkzeug.wrappers import response

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
        

        cmts = list(db.comment.find({},{'_id':False}))
        feeds = list(db.feed.find({},{'_id':False}).sort("date",-1))
        
        
        now_fd = [] # 계산된 시간 
        for i in range(len(feeds)):
            millis = int(round(time.time() * 1000))
            fd_time = feeds[i]['date']
            me_time = math.floor(((millis - fd_time)/(1000*60)))
            me_timehour = math.floor(((millis - fd_time)/(1000*60*60))%24)
            me_timeday = math.floor(((millis - fd_time)/(1000*60*60*24)))
            me_timeyear = math.floor(me_timeday / 365)

            if me_time < 1 :
                now_fd.append('방금전')
            elif me_time < 60 :
                a = str(me_time) + '분전'
                now_fd.append(a)

            
            elif me_timehour < 24 :
                a = str(me_timehour) + '시간전'
                now_fd.append(a)
            
            
            elif me_timeday < 365 :
                a = str(me_timeday) + '일전'
                now_fd.append(a)
            
            elif me_timeyear >= 1 : 
                a = str(me_timeyear) + '년전'
                now_fd.append(a)

        new_feeds=[] # 계산된 시간으로 새 리스트 
        dic = dict()
        for j in range(len(feeds)):
            feed_id = feeds[j]['id']
            feed_photo = feeds[j]['photo']
            feed_like = feeds[j]['like']
            feed_save = feeds[j]['save']
            feed_text = feeds[j]['text']
            feed_postid = feeds[j]['postid']
            feed_date = now_fd[j]
            feed_nick = feeds[j]['nick']
            feed_profile = feeds[j]['profile']
            dic = dict()
            dic[1] = feed_id
            dic[2] = feed_photo
            dic[3] = feed_like
            dic[4] = feed_save
            dic[5] = feed_text
            dic[6] = feed_postid
            dic[7] = feed_date
            dic[8] = feed_nick
            dic[9] = feed_profile
            new_feeds.append(dic)


        if user_pic != None:
            return render_template('feed_page.html', nickname = user_info['nick'], name = user_info['name'], image = user_pic['img'], cmts= cmts, feeds = new_feeds) 
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

    all_feed = list(db.feed.find({},{'_id':False}))

    #postid 를 db의 길이 + 1을하여 지정해줌 
    postid = len(all_feed) + 1

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

    return jsonify({'result':'success'})



@main.route("/addcmt", methods=["POST"])
def addcmt():

        comment_receive = request.form['comment_give']
        postid_receive = request.form['postid_give']
        print(postid_receive)
        token_receive = request.cookies.get('mytoken')

        payload = jwt.decode(token_receive, SECRET_KEY, algorithms='HS256')
        
        # 여기는 유저 DB
        user_info = db.user.find_one({'id': payload['id']})
        pic_info = db.pic.find_one({'id': payload['id']})
        


        nickname = user_info['nick']
        profile_pic = pic_info['img']

        doc = {'nick': nickname, 'cmt': comment_receive, 'cmtid': postid_receive, 'img': profile_pic}
        db.comment.insert_one(doc)
        print(comment_receive)
        return jsonify({'result':'댓글이 말대꾸?'})
    # except:
    #     return jsonify({'result':'허튼짓 금지'})



@main.route("/cmt")
def cmt():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms='HS256')
        
        user_info = db.user.find_one({'id': payload['id']})

        user_pic = db.pic.find_one({'id': payload['id']})
        

        cmts = list(db.comment.find({},{'_id':False}))
        
    
 
        if user_pic != None:
            return render_template('test.html', nickname = user_info['nick'], name = user_info['name'], image = user_pic['img'], cmts= cmts) 
        else :
            return render_template('test.html', nickname = user_info['nick'], name = user_info['name']) # 프로필 사진이 없을때.
    except jwt.ExpiredSignatureError:
        # 위를 실행했는데 만료시간이 지났으면 에러가 납니다.
        return redirect(url_for('login.home', msg =  '로그인 시간이 만료되었습니다.'))
    except jwt.exceptions.DecodeError:
        return redirect(url_for('login.home', msg = '로그인 정보가 존재하지 않습니다.'))







