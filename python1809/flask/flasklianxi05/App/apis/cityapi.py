import time

from flask_restful import Resource, fields, marshal_with

from App.models import *
'''
{
    'msg': '获取区域数据成功',
    'status': 200,
    'time': '4567891232',
    'data': {
        'A': [
            {
                'id': xxx,
                'parentId': xxx,
                'regionName': 'xxxx',
                'cityCode': xxxx,
                'pinYin': 'xxxx'
            }, {}, {}...],

        'B': [{}, {}, {}...],
        ....
    }
}
'''

city_fields={
    'id':fields.Integer,
    'parenId':fields.Integer,
    'regionName':fields.String,
    'cityCode':fields.Integer,
    'pinYin':fields.String,
}
letter_fields={
    'A':fields.List(fields.Nested(city_fields))
}
result_fields={
    'msg':fields.String,
    'status':fields.Integer,
    'time':fields.String,
    'data':fields.Nested(letter_fields)
}
class CityResource(Resource):
    @marshal_with(result_fields)
    def get(self):

        letters=Letter.query.all()
        print(letters)
        response_data={
            'msg':'获取数据成功',
            'status':200,
            'time':str(int(time.time()))

        }
        data={}
        for letter in letters:
            print('#########')
            print(letter)
        return response_data
