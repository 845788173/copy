from flask import render_template
from flask_mail import Message
from flask_restful import reqparse, fields, Resource, marshal_with
from werkzeug.security import check_password_hash

from App.ext import mail, cache, db
from App.models import User
from tools import format_response, get_token

parser=reqparse.RequestParser()
parser.add_argument('email',type=str,required=True,help='email')
parser.add_argument('password',type=str,required=True,help='password')

class IconForm(fields.Raw):
    def format(self, value):
        return '/static/img/' + value
user_fields={
    'name':fields.String,
    'token':fields.String,
    'icon':IconForm(attribute='icon'),
    'permissions':fields.Integer,
}

result_fields={
    'msg':fields.String,
    'time':fields.String,
    'status':fields.Integer,
    'err':fields.String(default=''),
    'data':fields.Nested(user_fields,default='')
}

class Login(Resource):
    @marshal_with(result_fields)
    def post(self):
        parse=parser.parse_args()
        email=parse.get('email')
        password=parse.get('password')
        responseData={

        }
        users=User.query.filter(User.email==email)
        if users.count>0:
            user=users.first()
            if user.isdelete==True:
                return format_response(msg='该用户已被登录',status=404,err='')
            if check_password_hash(user.password,password):
                if user.active==False:
                    msg=Message(subject='TPP激活邮件',
                                recipients=[user.email]
                                )
                    active_url='http://127.0.0.1:5000/api/v1/register/?token=' +user.token
                    body_html=render_template('useractive.html',name=user.name,)
                    msg.html=body_html
                    mail.send(msg)
                    cache.set(user.token,user.id,timeout=30)
                    return format_response(msg='登录失败',status='406',err='该用户尚未激活，请激活(激活邮件已发送成功)')
                user.token=get_token()
                db.session.add(user)
                db.session.commit()




