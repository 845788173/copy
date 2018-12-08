from flask_restful import Resource, fields, marshal_with, reqparse

# 请求参数 定制
from app.ext import  db
from app.models import User
from app.tools import format_response, get_token

parser = reqparse.RequestParser()
parser.add_argument('phone', type=str, required=True, help='请带入手机号')
parser.add_argument('randomint', type=int, required=True, help='请带入短信验证码')

# 响应数据 定制
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


class SmsLogin(Resource):
    @marshal_with(result_fields)
    def post(self):
        # 获取参数
        parse = parser.parse_args()
        phone = parse.get('phone')
        randomint = parse.get('randomint')

        # # 缓存中 取出 验证码
        # cache_randomint = cache.get(phone)
        # if cache_randomint: # 没超时
        #     if cache_randomint == randomint:    # 验证通过
        #         user = User.query.filter(User.phone==phone)
        #
        #
        #         user.token = get_token()
        #         db.session.add(user)
        #         db.session.commit()
        #
        #         # 删除短信验证码
        #         cache.delete(phone)
        #
        #         return format_response(msg='登录成功', status=200, data=user)
        #     else:   # 验证未通过
        #         return format_response(msg='登录失败', status=400, err='验证码输入错误')
        # else:   # 已超时
        #     return format_response(msg='登录失败', status=400, err='短信验证超时')