from flask_restful import Resource, fields, marshal_with, marshal
from app.models import City,Letter

'''
{
    'msg': '获取区域数据成功',
    'status': 200,
    'time': '4567891232',
    'data': {
        'A':[
            {
                'id': xxx,
                'parentId': xxx,
                'regionName': 'xxxx',
                'cityCode': xxxx,
                'pinYin': 'xxxx'
            },{},{}...],
            
        'B':[{},{},{}...],
        ....
    }
}
'''


## 方式一
# city_fields = {
#     'id': fields.Integer,
#     'parentId': fields.Integer,
#     'regionName': fields.String,
#     'cityCode': fields.Integer,
#     'pinYin': fields.String
# }
#
# letter_fields = {
#     'A': fields.List(fields.Nested(city_fields)),
#     'B': fields.List(fields.Nested(city_fields)),
#     'C': fields.List(fields.Nested(city_fields)),
#     'D': fields.List(fields.Nested(city_fields)),
#     'E': fields.List(fields.Nested(city_fields)),
#     'F': fields.List(fields.Nested(city_fields)),
#     'G': fields.List(fields.Nested(city_fields)),
#     'H': fields.List(fields.Nested(city_fields)),
#     'J': fields.List(fields.Nested(city_fields)),
#     'K': fields.List(fields.Nested(city_fields)),
#     'L': fields.List(fields.Nested(city_fields)),
#     'M': fields.List(fields.Nested(city_fields)),
#     'N': fields.List(fields.Nested(city_fields)),
#     'P': fields.List(fields.Nested(city_fields)),
#     'Q': fields.List(fields.Nested(city_fields)),
#     'R': fields.List(fields.Nested(city_fields)),
#     'S': fields.List(fields.Nested(city_fields)),
#     'T': fields.List(fields.Nested(city_fields)),
#     'W': fields.List(fields.Nested(city_fields)),
#     'X': fields.List(fields.Nested(city_fields)),
#     'Y': fields.List(fields.Nested(city_fields)),
#     'Z': fields.List(fields.Nested(city_fields)),
# }
#
# result_fileds = {
#     'msg': fields.String,
#     'status': fields.Integer,
#     'time': fields.String,
#     'data': fields.Nested(letter_fields)
# }
#
# import time
# class CityResource(Resource):
#     @marshal_with(result_fileds)
#     def get(self):
#         letters = Letter.query.all()
#
#         responseData = {
#             'msg': '获取区域数据成功',
#             'status': 200,
#             'time': str(int(time.time())),
#         }
#
#         # data = {
#         #     'A': [],
#         #     'B': [],
#         # }
#         data = {}
#         for letter in letters:
#             # letter.name  >>  A、B.....
#             data[letter.name] = letter.l_cities
#
#         responseData['data'] = data
#
#         return responseData



## 方式二: 高级用法
city_fields = {
    'id': fields.Integer,
    'parentId': fields.Integer,
    'regionName': fields.String,
    'cityCode': fields.Integer,
    'pinYin': fields.String
}

import time
class CityResource(Resource):
    def get(self):
        # 获取所有字母
        letters = Letter.query.all()

        # 返回数据
        responseData = {
            'msg': '获取区域数据成功',
            'status': 200,
            'time': str(int(time.time())),
        }


        # 数据列表
        data = {}
        # 动态格式列表
        letter_fields_dynamic = {}


        # 遍历每个字母 对应 城市
        for letter in letters:
            # letter.name  >>>  A
            # letter.cities >>> [{},{},{}....]
            data[letter.name] = letter.l_cities
            letter_fields_dynamic[letter.name] = fields.List(fields.Nested(city_fields))

        # 最终的数据
        responseData['data'] = data
        # 最终的格式 【定制】
        result_fileds = {
            'msg': fields.String,
            'status': fields.Integer,
            'time': fields.String,
            'data': fields.Nested(letter_fields_dynamic)
        }

        # 格式化数据
        result = marshal(responseData, result_fileds)

        return result