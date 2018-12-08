import time

from flask import render_template
from flask_mail import Message
from flask_restful import Resource, marshal_with, fields, reqparse

# 请求参数 定制
from werkzeug.security import generate_password_hash

from app.ext import db, mail
from app.models import User
from app.tools import get_token, generate_password

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help='请填写用户名name')
parser.add_argument('password', type=str, required=True, help='请填写密码password')
parser.add_argument('email', type=str, required=True, help='请填写邮箱email')
parser.add_argument('phone', type=str, required=True, help='请填写手机phone')

# 响应格式 定制
'''
{
    'msg': '注册成功',
    'status': 200,
    'time': '2345678',
    'err': '',
    'data': {
        'name': 'atom',
        'token': '3456789dfghjikoertyu',
        'icon': '/static/img/head.png',
        'permissions': 1
    }
}
'''

# 自定义
class IconForm(fields.Raw):
    def format(self, value):
        return '/static/img/' + value

user_fileds = {
    'name': fields.String,
    'token': fields.String,
    # 'icon': fields.String,
    'icon': IconForm(attribute='icon'),
    'permissions': fields.Integer
}

result_fields = {
    'msg': fields.String,
    'status': fields.Integer,
    'time': fields.String,
    'err': fields.String(default=''),
    'data': fields.Nested(user_fileds, default='')
}

class UserRegister(Resource):
    @marshal_with(result_fields)
    def post(self):
        parse = parser.parse_args()

        # 用户信息
        user = User()
        user.name = parse.get('name')
        # user.password = generate_password(parse.get('password'))
        user.password = generate_password_hash(password=parse.get('password'))
        user.email = parse.get('email')
        user.phone = parse.get('phone')
        user.token = get_token()

        # 返回数据
        responseData = {
            'time': str(int(time.time()))
        }


        # 异常处理
        users = User.query.filter(User.email == user.email)
        if users.count()>0: # 已存在
            responseData['status'] = 406
            responseData['msg'] = '注册失败'
            responseData['err'] = '该邮箱已经被注册使用!'
            return responseData
        else:   # 不存在
            # 写入数据库
            db.session.add(user)
            db.session.commit()

            # 发送邮件
            msg = Message(subject="TPP激活邮件",  # 主题
                          # sender="18924235915@163.com",    # 发件人
                          recipients=[user.email]    # 收件人
                          )
            active_url = 'http://127.0.0.1:5000/api/v1/useractive/?token=' + user.token
            body_html = render_template('useractive.html', name=user.name, active_url=active_url)
            msg.html = body_html    # 邮件正文
            mail.send(msg)  # 发送操作

            # key:value  >>>  token:userid
            # 超时处理
            # cache.set(user.token, user.id, timeout=30)

            responseData['status'] = 200
            responseData['msg'] = '注册成功,请查看邮件(需要激活)!'
            responseData['data'] = user

            return responseData


