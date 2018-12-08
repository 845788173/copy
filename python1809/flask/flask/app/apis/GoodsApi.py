from flask_restful import Resource, reqparse

# 请求参数解析
parser = reqparse.RequestParser()
# required 是否必填参数
parser.add_argument('page', type=int, required=True, help='请求带入参数page')


class GoodsResource(Resource):
    def get(self):
        # 类比 request.args
        args = parser.parse_args()
        page = args.get('page')

        str = '[get]第%s页 数据获取完成' % page

        return {'msg':str}

    def post(self):
        # 类比 request.form
        args = parser.parse_args()
        page = args.get('page')
        str = '[post]第%s页 数据获取完成' % page

        return {'msg': str}