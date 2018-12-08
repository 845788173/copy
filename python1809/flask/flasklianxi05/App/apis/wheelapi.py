from flask_restful import Resource, fields, marshal_with


## 请求格式定制


## 响应格式定制
from App.models import Wheel

'''
{
    'msg': '获取轮播图数据成功',
    'status': 200,
    'count': 5,
    'time': '456789056789',
    'data': [
        {
            'img': 'xxx.jpg',
            'name': 'xxxx',
            'trackid': '123123'
        },
        {},
        ...
    ]
}
'''

wheel_fields = {
    'img': fields.String,
    'name': fields.String,
    'trackid': fields.String
}

result_fields = {
    'msg': fields.String,
    'status': fields.Integer(default=400),
    'count': fields.Integer,
    'time': fields.String,
    'data': fields.List(fields.Nested(wheel_fields))
}

import time
class WhellResource(Resource):
    @marshal_with(result_fields)
    def get(self):
        wheels = Wheel.query.all()

        responseData = {
            'msg': '获取轮播图数据成功',
            'status': 200,
            'count': len(wheels),
            'time': str(int(time.time())),
            'data': wheels,
            'title': 'axf',
        }

        return responseData
