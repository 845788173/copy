from flask_restful import Resource, reqparse, marshal_with, fields

# 请求格式 定制
from werkzeug.security import generate_password_hash, check_password_hash

from app.ext import db
from app.models import User
from app.tools import format_response

parser = reqparse.RequestParser()
parser.add_argument('token', type=str, required=True, help='请填写token')
parser.add_argument('oldpd', type=str, required=True, help='请填写旧密码oldpd')
parser.add_argument('newpd', type=str, required=True, help='请填写新密码newpd')

# 响应格式 定制
result_fields = {
    'msg': fields.String,
    'status': fields.Integer,
    'time': fields.String,
    'err': fields.String(default=''),
}


class PasswordResource(Resource):
    @marshal_with(result_fields)
    def post(self):
        # 获取数据
        parse = parser.parse_args()
        token = parse.get('token')
        oldpd = parse.get('oldpd')
        newpd = parse.get('newpd')

        user = User.query.filter(User.token == token).first()

        if check_password_hash(user.password, oldpd):
            user.password = generate_password_hash(newpd)
            db.session.add(user)
            db.session.commit()
            return format_response(msg='修改密码成功', status=200)
        else:
            return format_response(msg='修改密码失败', status=400, err='旧密码输入有误')