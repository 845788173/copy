from flask_restful import reqparse, fields, Resource, marshal_with

from App.ext import db
from App.models import User
from App.tools import get_token

parser = reqparse.RequestParser()
parser.add_argument('username',required=True, type=str,  help='请填写username')
parser.add_argument('password',required=True, type=str, help='请填写email')
parser.add_argument('email',required=True, type=str,  help='请填写密码password')



user_fileds = {
    'username': fields.String,
    'password': fields.String,
    'email': fields.String,
    'token': fields.String,

}

result_fields = {
    'msg': fields.String,
    'status': fields.Integer,
    'err': fields.String(default=''),
    'data': fields.Nested(user_fileds, default='')
}

class Register(Resource):
    @marshal_with(result_fields)
    def post(self):
        print('1111')

        parse = parser.parse_args()
        print('22222')
        user=User()
        user.username=parse.get('username')

        user.password=parse.get('password')
        user.email=parse.get('email')
        user.token=get_token()
        print(user.email)
        print(user.username)
        print(user.password)
        responseData={}
        print('@@@@@')
        users = User.query.filter(User.email == user.email)
        print('$$$$$$')
        if users.count() > 0:  # 已存在
            responseData['status'] = 406
            responseData['msg'] = '注册失败'
            responseData['err'] = '该邮箱已经被注册使用!'
            return responseData
        else:  # 不存在
            # 写入数据库
            print('****')
            db.session.add(user)
            print('&&&&')
            db.session.commit()
            print('^^^^')
            responseData['status'] = 200
            responseData['msg'] = '注册成功,请查看邮件(需要激活)!'
            responseData['data'] = user
            return responseData


