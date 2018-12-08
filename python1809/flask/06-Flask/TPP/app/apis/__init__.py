from flask_restful import Api

from app.apis.CityApi import CityResource
from app.apis.HelloApi import HelloWorld

api = Api()

def init_api(app):
    api.init_app(app)


api.add_resource(HelloWorld, '/api/v1/hello/')
api.add_resource(CityResource, '/api/v1/city/')