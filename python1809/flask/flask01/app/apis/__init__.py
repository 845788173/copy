from flask_restful import Api

from app.apis.HelloApi import HelloWorld
from app.apis.WheelApi import WhellResource

api = Api()

def init_api(app):
    api.init_app(app)



# 添加资源
api.add_resource(HelloWorld, '/api/v1/hello/')
api.add_resource(WhellResource, '/api/v1/wheel/')