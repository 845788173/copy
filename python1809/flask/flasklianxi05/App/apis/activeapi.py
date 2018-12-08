import time

from flask_restful import fields, Resource, marshal_with, reqparse

from App.ext import cache, db
from App.models import User
from tools import get_token

parser=reqparse.RequestParser()
parser.add_argument('token',type=str,required=True,help='请输入令牌token')

user_fields={
    'name':fields.String,
    'token':fields.String,
    'icon':fields.String,
    'permissions':fields.String,
}
result_fields={
    'status':fields.Integer,
    'msg':fields.String,
    'time':fields.String,
    'err':fields.String(default=''),
    'data':fields.Nested(user_fields,default=''),
}


class UserActive(Resource):
    @marshal_with(result_fields)
    def get(self):
        parse=parser.parse_args()
        token=parse.get('token')
        userid=cache.get(token)
        if not userid:
            responseData={
                'status':402,
                'msg':'激活失败',
                'err':'请与管理员联系',
                'time':str(int(time.time()))
            }
            return responseData
        else:
            user=User.query.get(userid)
            user.isactive=True
            user.token=get_token()
            db.session.add(user)
            db.session.commit()
            responseData={
                'status':200,
                'msg':'用户激活成功',
                'data':user,
                'time':str(int(time.time()))
            }
            return responseData



