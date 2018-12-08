from flask_restful import Resource, fields, marshal_with

from App.models import *

# parser=reqparse.RequestParser()
# parser.add_argument('image',required=True,type=str)

user_fileds = {
    'image': fields.String,


}

result_fields = {
    'msg': fields.String,
    'status': fields.Integer,
    'err': fields.String(default=''),
    'data': fields.Nested(user_fileds, default='')
    # 'data':fields.Nested()
}


class lunbo(Resource):
    @marshal_with(result_fields)
    def get(self):
        # parse=parser.parse_args()


        images=Lunbo.query.all()
        # print(type(images))
        responseData={}
        responseData['data']=images
        print(type(responseData['data']))

        return responseData


