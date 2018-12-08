from flask_restful import Resource, fields, marshal_with
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

city_fields = {
    'id': fields.Integer,
    'parentId': fields.Integer,
    'regionName': fields.String,
    'cityCode': fields.Integer,
    'pinYin': fields.String
}

letter_fields = {
    'A': fields.List(fields.Nested(city_fields)),
    'B': fields.List(fields.Nested(city_fields)),
    'C': fields.List(fields.Nested(city_fields))
}

result_fileds = {
    'msg': fields.String,
    'status': fields.Integer,
    'time': fields.String,
    'data': fields.Nested(letter_fields)
}

import time
class CityResource(Resource):
    @marshal_with(result_fileds)
    def get(self):
        letters = Letter.query.all()

        responseData = {
            'msg': '获取区域数据成功',
            'status': 200,
            'time': str(int(time.time())),
        }

        # data = {
        #     'A': [],
        #     'B': [],
        # }
        data = {}
        for letter in letters:
            # letter.name  >>  A、B.....
            data[letter.name] = letter.l_cities

        responseData['data'] = data

        return responseData