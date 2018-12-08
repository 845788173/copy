import hashlib
import time
import uuid

from flask import render_template
from flask_mail import Message
from flask_restful import Resource, marshal_with, fields, reqparse

# 请求参数 定制
from werkzeug.security import check_password_hash

from app.ext import mail, db
from app.models import User
from app.tools import get_token, format_response, generate_password

parser = reqparse.RequestParser()
parser.add_argument('email', type=str, required=True, help='请带入email')
parser.add_argument('password', type=str, required=True, help='请带入password')

# 响应数据 定制
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

class Login(Resource):
    @marshal_with(result_fields)
    def post(self):
        parse = parser.parse_args()
        email = parse.get('email')
        password = parse.get('password')

        responseData = {
            'time': str(int(time.time()))
        }

        # 邮箱校验
        users = User.query.filter(User.email == email)
        if users.count()>0: # 存在

            # 获取对应用户
            user = users.first()

            # 是否被删除
            if user.isdelete == True:
                return format_response(msg='登录失败', status=401, err='该用户已被注销')

            # 密码校验
            #if user.password == generate_password(password):
            if check_password_hash(user.password, password):  #  密码正确
                if user.isactive == False:  # 未激活
                    # 发邮件
                    msg = Message(subject="TPP激活邮件",  # 主题
                                  # sender="18924235915@163.com",    # 发件人
                                  recipients=[user.email]  # 收件人
                                  )
                    active_url = 'http://127.0.0.1:5000/api/v1/useractive/?token=' + user.token
                    body_html = render_template('useractive.html', name=user.name, active_url=active_url)
                    msg.html = body_html  # 邮件正文
                    mail.send(msg)  # 发送操作

                    # 超时处理
                    # cache.set(user.token, user.id, timeout=30)

                    return format_response(msg='登录失败', status=401, err='用户还未激活，请激活后登录(激活邮件已发送成功)!')

                # 成功操作
                user.token = get_token()
                db.session.add(user)
                db.session.commit()

                return format_response(data=user, msg='登录成功', status=200)

            else:   # 密码错误
                return format_response(msg='登录失败', status=401, err='密码错误')

        else:   # 不存在
            return format_response(msg='登录失败', status=401, err='邮箱不存在')