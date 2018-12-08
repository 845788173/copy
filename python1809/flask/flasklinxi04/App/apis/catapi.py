import time

from flask_restful import Resource, fields, marshal_with

from App.models import *

one_fields={
    'name':fields.String,
    'color':fields.String,
    'age':fields.Integer
}

resource_fields={
    'msg':fields.String,
    'status':fields.Integer,
    'time':fields.String,
    'data':fields.Nested(one_fields)

}

class Onecatresource(Resource):
    @marshal_with(resource_fields)
    def get(self):
        cat=Cat.query.first()

        responseData = {
            'msg': '获取Cat数据成功',
            'status': 200,
            'time': str(int(time.time())),
            'data': cat
        }

        return responseData