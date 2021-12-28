from flask import Flask , render_template, request, jsonify

from pymongo import MongoClient


def create_app():
    app = Flask(__name__)


    @app.route('/')
    def home():
        # return render_template('index.html')
        return 'hello, insta'

    return app