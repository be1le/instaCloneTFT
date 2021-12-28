from flask import render_template, request, url_for, session, redirect, jsonify
from flask.blueprints import Blueprint

from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.0pi7g.mongodb.net/Cluster0?retryWrites=true&w=majority')  # 클라이언트 설정시 작성
db = client.dbsparta

import hashlib

sign_up = Blueprint("sign_up", __name__ , url_prefix="/sign", static_folder="static", template_folder="templates")


@sign_up.route("/")
def sign():
    return render_template("sign_up.html")


@sign_up.route("/register", methods=['POST'])
def register():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    nickname_receive = request.form['nickname_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    db.user.insert_one({'id': id_receive, 'pw': pw_hash, 'nick': nickname_receive})

    return jsonify({'result': 'success'})


# id , pw , pw확인조건 수정하기