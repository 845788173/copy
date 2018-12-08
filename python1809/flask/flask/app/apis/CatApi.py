from flask_restful import Resource, fields, marshal_with
from app.models import Cat
import time

# 返回给客户端的数据 【一只】
'''
{
    'msg':'获取Cat数据成功',
    'status': 200,
    'time': '3456789567',
    'data': {
        'name': '旺财',
        'color': '土豪金',
        'age': 8
    }
}
'''
# class OneCatResource(Resource):
#     def get(self):
#         cat = Cat.query.first()
#
#         responseData = {
#             'msg': '获取Cat数据成功',
#             'status': 200,
#             'time': str(int(time.time())),
#             'data': {
#                 'name': cat.name,
#                 'color': cat.color,
#                 'age': cat.age
#             }
#         }
#
#         return responseData

### 数据格式化操作
# 定制格式
# 字符串 fields.String
# 整形 fields.Integer
# 列表 fields.List
# 级联数据(字典) fields.Nested

onecat_fields = {
    'name': fields.String,
    'color': fields.String,
    'age': fields.Integer
}

# 以格式化定制为标准
# 返回数据 比 定制的 字段要多  多余的字段会被过滤
# 返回数据 比 定制的 字段要少  多余的字段会显示为null
resource_fileds = {
    'msg': fields.String,
    'status': fields.Integer,
    'time': fields.String,
    'data': fields.Nested(onecat_fields),
    'haha': fields.String
}

class OneCatResource(Resource):
    @marshal_with(resource_fileds)
    def get(self):
        cat = Cat.query.first()

        responseData = {
            'msg': '获取Cat数据成功',
            'status': 200,
            'time': str(int(time.time())),
            'data': cat
        }

        return responseData









# 返回给客户端的数据 【多只】
'''
{
    'msg':'获取Cat数据成功',
    'status': 200,
    'time': '3456789567',
    'data': [
        {
            'name': '旺财',
            'color': '土豪金',
            'age': 8
        },
        {
            'name': '旺财',
            'color': '土豪金',
            'age': 8
        }
        ...
    ]
}
'''
# class MoreCatResource(Resource):
#     def get(self):
#         cats = Cat.query.all()
#
#         responseData = {
#             'msg': '获取Cat数据成功',
#             'status': 200,
#             'time': str(int(time.time())),
#             'data': [   # 能不能直接写cats???
#                 {
#                     'name': cats[0].name,
#                     'color': cats[0].color,
#                     'age': cats[0].age
#                 },
#                 {
#                     'name': cats[1].name,
#                     'color': cats[1].color,
#                     'age': cats[1].age
#                 },
#                 {
#                     'name': cats[2].name,
#                     'color': cats[2].color,
#                     'age': cats[2].age
#                 },
#                 {
#                     'name': cats[3].name,
#                     'color': cats[3].color,
#                     'age': cats[3].age
#                 },
#                 {
#                     'name': cats[4].name,
#                     'color': cats[4].color,
#                     'age': cats[4].age
#                 },
#             ]
#         }
#
#         return responseData


catmodel_fields = {
    'name': fields.String,
    'color': fields.String,
    'age': fields.Integer
}
result_fileds = {
    'msg': fields.String,
    'status': fields.Integer,
    'time': fields.String,
    'data': fields.List(fields.Nested(catmodel_fields))
}
class MoreCatResource(Resource):
    @marshal_with(result_fileds)
    def get(self):
        cats = Cat.query.all()

        responseData = {
            'msg': '获取Cat数据成功',
            'status': 200,
            'time': str(int(time.time())),
            'data': cats
        }

        return responseData

