from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help='请填写username')
parser.add_argument('email', type=str, required=True, help='请填写email')
parser.add_argument('password', type=str, required=True, help='请填写密码password')