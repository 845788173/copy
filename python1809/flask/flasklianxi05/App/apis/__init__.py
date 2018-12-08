from flask_restful import Api

from App.apis.cityapi import CityResource
from App.apis.registerapi import UserRegister
from App.apis.wheelapi import WhellResource

api=Api()
def init_api(app):
    api.init_app(app)


api.add_resource(CityResource ,'/api/v1/city/')
api.add_resource(WhellResource,'/api/v1/wheel/')
api.add_resource(UserRegister,'/api/v1/register/')