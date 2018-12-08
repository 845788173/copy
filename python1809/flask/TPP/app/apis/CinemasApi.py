from flask_restful import Resource, fields, marshal_with, reqparse

# 请求参数 定制
from app.models import Cinemas
from app.tools import format_response

parser = reqparse.RequestParser()
parser.add_argument('city', type=str, default='全部')
parser.add_argument('district', type=str)
parser.add_argument('sort', type=int, default=1)    # 1按评分倒序， 2按评分升序
parser.add_argument('limit', type=int)

# 响应格式 定制
cinemas_files = {
    'name' : fields.String,
    'city' : fields.String,
    'district' : fields.String,
    'address' : fields.String,
    'phone' : fields.String,
    'score' : fields.Float,
    'hallnum' : fields.Integer,
    'servicecharge' : fields.Float,
    'astrict' : fields.Integer,
}

result_fields = {
    'msg': fields.String,
    'status': fields.Integer,
    'time': fields.String,
    'err': fields.String(default=''),
    'data': fields.List(fields.Nested(cinemas_files))
}

class CinemasResource(Resource):
    @marshal_with(result_fields)
    def get(self):
        parse = parser.parse_args()
        city = parse.get('city')
        district = parse.get('district')
        sort = parse.get('sort')
        limit_n = parse.get('limit')

        if city == '全部':
            cinemas = Cinemas.query.all()

        else:
            cinemas = Cinemas.query.filter(Cinemas.city == city)


        if district:
            cinemas = cinemas.filter(Cinemas.district == district)

        if sort == 1:
            cinemas = cinemas.order_by(-Cinemas.score)
        elif sort == 2:
            cinemas = cinemas.order_by(Cinemas.score)

        if limit_n:
            cinemas = cinemas.limit(limit_n)

        return format_response(msg='获取影院信息成功', status=200, data=cinemas)