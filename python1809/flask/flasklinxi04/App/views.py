import hashlib
import time
import uuid

from flask import Blueprint, jsonify, request

from App.models import *

blue=Blueprint('blue',__name__)


def init_blue(app):
    app.register_blueprint(blueprint=blue)

@blue.route('/jsontest/')
def jsontest():
    data={
        'name':'xiaoming',
        'age':16,
    }
    return jsonify(data)


def generate_password(password):
    hash=hashlib.sha256()
    hash.update(password.encode())
    return hash.hexdigest()


def get_token():
    hash=hashlib.sha512()
    sha_str=str(uuid.uuid4())+str(int(time.time()))
    hash.update(sha_str.encode())
    return hash.hexdigest()



@blue.route('/api/v1/user/',methods=['GET','POST','PUT'])
def user():
    responseData={
        'status':400,
        'error':'',
        'time':str(int(time.time())),
        'data':'',
        'msg':'',
    }
    if request.method=='GET':
        pass
    elif request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        if not username or not password:
            responseData['status']=406
            responseData['error']='yonghumingkoumimaweikong'
            responseData['msg']='zhuceshibai'
            return jsonify(responseData)
        else:
            user=User()
            user.username=username
            user.password=generate_password(password)
            user.token=get_token()
            try:
                db.session.add(user)
                db.session.commit()
                responseData['msg']='zhucechenggong'
                responseData['status']=200
                responseData['data']={
                    'username':user.username,
                    'token':user.token,
                }
                return jsonify(responseData)
            except Exception as fp:
                responseData['msg']='zhuceshnbai'
                responseData['status']=422
                responseData['error']='yonghumingyicunzai'
                return jsonify(responseData)
    elif request.method=='PUT':
        pass


