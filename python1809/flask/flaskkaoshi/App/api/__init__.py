from flask_restful import Api

from App.api.lunboapi import lunbo
from App.api.registerapi import Register

api=Api()


def init_api(app):
    api.init_app(app)


api.add_resource(lunbo,'/api/v1/lunbo/')
api.add_resource(Register,'/api/v1/register/')
# api.add_resource(lunbo1,'/api/v1/lunbo/')