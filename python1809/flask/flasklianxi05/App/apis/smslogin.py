from flask_restful import reqparse, fields, Resource, marshal_with

from App.ext import cache, db
from App.models import User
from tools import get_token

parser = reqparse.RequestParser()
parser.add_argument('phone', type=str, required=True, help='请带入手机号')
parser.add_argument('randomint', type=int, required=True, help='请带入短信验证码')

class IconForm(fields.Raw):
    def format(self, value):
        return '/static/img/' +value




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
    def get(self):
        parse=parser.parse_args()
        phone=parse.get('phone')
        randomint=parse.get('randomint')
        cache_randomint=cache.get('phone')
        if cache_randomint:
            if cache_randomint==randomint:
                user=User.query.filter(User.phone==phone).first()
                user.token=get_token()
                db.session.add(user)
                db.session.commit()


                cache.delete(phone)

