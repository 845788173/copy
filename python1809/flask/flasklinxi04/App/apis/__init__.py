from flask_restful import Api

from App.apis.Goodsapi import GoodsResource
from App.apis.catapi import Onecatresource
from App.apis.helloapi import Helloworld
from App.apis.nameapi import Nameresource

api=Api()

def init_api(app):
    api.init_app(app=app)


api.add_resource(Nameresource,'/api/v1/name/<str>/')
api.add_resource(Helloworld,'/api/v2/hello/',endpoint='helloword')
api.add_resource(GoodsResource,'/api/v3/goods/')
api.add_resource(Onecatresource,'/api/v4/cat/')