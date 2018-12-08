from flask_restful import Resource


class Nameresource(Resource):
    def get(self,str):
        return {'msg': 'nidmingzi'+str}