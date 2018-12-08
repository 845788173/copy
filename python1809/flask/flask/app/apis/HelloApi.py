from flask_restful import Resource

# 定义资源
class HelloWorld(Resource):
    def get(self):  # get请求
        return {'msg':'get请求'}

    def post(self): # post请求
        return {'msg': 'post请求'}

