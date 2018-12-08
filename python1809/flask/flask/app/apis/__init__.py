from flask_restful import Api

from app.apis.CatApi import OneCatResource, MoreCatResource
from app.apis.GoodsApi import GoodsResource
from app.apis.HelloApi import HelloWorld
from app.apis.NameApi import NameResource

api = Api()

def init_api(app):
    api.init_app(app)

# 添加资源
api.add_resource(HelloWorld, '/api/v1/hello/', '/hehe/', '/haha/', '/zhangsan/', endpoint='helloworld')

api.add_resource(NameResource,'/api/v1/name/<str>/')

api.add_resource(GoodsResource, '/api/v1/goods/')

api.add_resource(OneCatResource, '/api/v1/cat/')

api.add_resource(MoreCatResource, '/api/v1/cats/')