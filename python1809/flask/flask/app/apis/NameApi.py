from flask_restful import Resource


class NameResource(Resource):
    def get(self, str):
        return {'msg':'你的名字'+str}
