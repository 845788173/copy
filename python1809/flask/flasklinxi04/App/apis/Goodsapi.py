from flask_restful import reqparse, Resource

parser=reqparse.RequestParser()

parser.add_argument('page',type=int,required=True,help='qingqiudairucanshuhelp')


class GoodsResource(Resource):
    def get(self):
        args=parser.parse_args()
        page=args.get('page')
        str='[get]di %sye,shujuwancheng'%page
        return {'msg':str}
    def post(self):
        args=parser.parse_args()
        page=args.get('page')
        str='[post]di%s,shujuwancheng'%page
        return {'msg':str}