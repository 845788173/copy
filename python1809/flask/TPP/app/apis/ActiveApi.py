import hashlib
import uuid

from flask_restful import Resource, marshal_with, fields, reqparse

# 请求参数 定制
from app.ext import db
from app.models import User

parser = reqparse.RequestParser()
parser.add_argument('token', type=str, required=True, help='token')

# 响应格式 定制
user_fileds = {
    'name': fields.String,
    'token': fields.String,
    'icon': fields.String,
    'permissions': fields.Integer
}

result_fields = {
    'msg': fields.String,
    'status': fields.Integer,
    'time': fields.String,
    'err': fields.String(default=''),
    'data': fields.Nested(user_fileds, default='')
}

class UserAcitve(Resource):
    @marshal_with(result_fields)
    def get(self):
        # 获取token
        parse = parser.parse_args()
        token = parse.get('token')

        # 去缓存中去取 userid
        userid = cache.get(token)
        if not userid:  # 不存在
            responseData = {
                'msg': '用户激活失败',
                'status': 200,
                'time': str(int(time.time())),
                'err': '链接已超时，请联系管理员!'
            }

            return responseData

        # 获取用户
        # user = User.query.filter(User.token == token).first()
        user = User.query.get(userid)

        # 改变状态
        user.isactive = True
        user.token = get_token()
        db.session.add(user)
        db.session.commit()

        responseData = {
            'msg': '用户激活成功',
            'status': 200,
            'time': str(int(time.time())),
            'data': user
        }

        return responseData



import time
def get_token():
    hash = hashlib.sha512()
    hash_str = str(uuid.uuid4()) + str(int(time.time()))
    hash.update(hash_str.encode('utf-8'))
    return hash.hexdigest()