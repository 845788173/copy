from flask_restful import Resource, marshal_with, fields, reqparse

# 请求参数 定制
from app.models import Movies
from app.tools import format_response

parser = reqparse.RequestParser()
# flag=0 默认值，全部        flag=1热映      flag=2即将上映
parser.add_argument('flag', type=int, default=0)
# top=0 默认值，全部        top=1取前5条数据
parser.add_argument('top', type=int, default=0)

# 响应格式
movie_fields = {
    'showname' : fields.String,
    'shownameen' : fields.String,
    'director' : fields.String,
    'leadingRole' : fields.String,
    'type' : fields.String,
    'country' : fields.String,
    'language' : fields.String,
    'duration' : fields.Integer,
    'screeningmodel' : fields.String,
    'openday' : fields.String,
    'backgroundpicture' : fields.String,
}

result_fields = {
    'msg': fields.String,
    'status': fields.Integer,
    'time': fields.String,
    'err': fields.String(default=''),
    'data': fields.List(fields.Nested(movie_fields))
}


class MovieResource(Resource):
    @marshal_with(result_fields)
    def get(self):
        # 参数
        parse = parser.parse_args()
        flag = parse.get('flag')
        top = parse.get('top')

        if flag:    # 过滤
            movie = Movies.query.filter(Movies.flag == flag)
        else:   # 全部
            movie = Movies.query.all()

        if top: # 取前5条
            movie = movie.limit(5)

        return format_response(msg='获取电影信息列表成功', status=200, data=movie)