import hashlib
import uuid

from flask import Blueprint, jsonify, request
from flask_restful import Resource

from app.ext import db
from app.models import User
import time

blue = Blueprint('blue', __name__)

def init_blue(app):
    app.register_blueprint(blueprint=blue)


@blue.route('/')
def index():
    return 'hello flask'



@blue.route('/jsontest/')
def jsontest():
    data = {
        'status': 200,
        'msg':'获取数据成功'
    }

    return jsonify(data)



# www.baidu.com/api/v2/
# api.baidu.com/v2/
# https://api.douban.com/v2/movie/search?tag=你是谁

@blue.route('/students/')
def students():

    responseData = [
        {
            'id': 1001,
            'name': '张三',
            'age': 18
        },
        {
            'id': 1002,
            'name': '李四',
            'age': 17
        },
        {
            'id': 1003,
            'name': '王五',
            'age': 22
        },
    ]

    return jsonify(responseData)


@blue.route('/api/v1/student/')
def stu1():
    pass

@blue.route('/api/v2/student/')
def stu2():
    pass


def generate_password(password):
    hash = hashlib.sha256()
    hash.update(password.encode('utf-8'))
    return hash.hexdigest()

def get_token():
    # 用户名  +　时间戳
    # uuid + 时间戳
    hash = hashlib.sha512()
    sha_str = str(uuid.uuid4()) + str(int(time.time()))
    hash.update(sha_str.encode('utf-8'))
    return hash.hexdigest()


@blue.route('/api/v1/user/', methods=['GET','POST','PUT','DELETE'])
def user():
    responseData = {
        'time': str(int(time.time())),
        'status': 400,
        'msg': '',
        'data': '',
        'error': ''
    }

    if request.method == 'GET': # 获取用户
        pass
    elif request.method == 'POST':  # 添加用户
        # 获取用户信息
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:    # 参数错误
            responseData['msg'] = '注册失败'
            responseData['error'] = '用户名或密码为空'
            responseData['status'] = 406
            return jsonify(responseData)
        else:   # 参数没问题
            user = User()
            user.username = username
            user.password = generate_password(password)
            user.token = get_token()

            try:    # 成功
                db.session.add(user)
                db.session.commit()
                responseData['msg'] = '注册成功'
                responseData['status'] = 200
                responseData['data'] = {
                    'username' : user.username,
                    'token': user.token
                }
                return jsonify(responseData)
            except Exception as ex: # 失败
                responseData['msg'] = '注册失败'
                responseData['status'] = 422
                responseData['error'] = '用户名已存在'
                return jsonify(responseData)

    elif request.method == 'PUT':   # 更新用户
        pass
    elif request.method == 'DELETE':    # 删除用户
        pass


