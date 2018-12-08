from flask_restful import Resource


class Helloworld(Resource):
    def get(self):
        return {'msg':'getqingqiu'}

    def post(self):
        return {'msg':'postqingqiu'}