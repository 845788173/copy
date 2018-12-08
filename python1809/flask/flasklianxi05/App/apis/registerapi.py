from flask import render_template
from flask_mail import Message
from flask_restful import reqparse, fields, Resource,  marshal_with
from werkzeug.security import generate_password_hash

from App.ext import db, mail, cache
from App.models import User
from tools import get_token

parser=reqparse.RequestParser()
parser.add_argument('name',type=str,required=True,help='请填写用户名name')
parser.add_argument('password',type=str,required=True,help='请填写密码password')
parser.add_argument('email',type=str,required=True,help='请填写邮箱email')
parser.add_argument('phone',type=str,required=True,help='请填写手机phone')


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
class IconForm(fields.Raw):
    def format(self, value):
        return 'static/img'+value

user_fields={
    'name':fields.String,
    'token':fields.String,
    'icon':IconForm(attribute='icon'),
    'permissions':fields.Integer,
}

fesult_fields={
    'msg':fields.String,
    'status':fields.Integer,
    'time':fields.String,
    'err':fields.String,
    'data':fields.Nested(user_fields)
}

class UserRegister(Resource):
    @marshal_with(fesult_fields)
    def post(self):
        parse=parser.parse_args()
        user=User()
        user.name=parse.get('name')
        user.phone=parse.get('phone')
        user.email=parse.get('email')
        user.password=generate_password_hash(password=parse.get('password'))
        user.token=get_token()
        responseData={}

        users=User.query.filter(User.email==user.email)
        if users.count>0:
            responseData['status']=406
            responseData['msg']='注册失败'
            responseData['err']='邮箱已注册'
        else:
            db.session.add(user)
            db.session.commit()
            mas=Message(subject='TPP激活邮件',
                        recipients=[user.email]
                        )
            url_active='http://127.0.0.1:5000/api/v1/register/?token='+user.token
            body_html=render_template('useractive.html',name=user.name,url_active=url_active)
            mas.html=body_html
            mail.send(mas)
            cache.set(user.token,user.id,timeout=60*60)
            responseData['status']=200
            responseData['msg']='注册成功请逐一查收（需要激活）'
            responseData['data']=user
            return responseData
