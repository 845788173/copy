from flask_restful import Api

from app.apis.ActiveApi import UserAcitve
from app.apis.CinemasApi import CinemasResource
from app.apis.CityApi import CityResource
from app.apis.FileApi import UploadHeadFile
from app.apis.HelloApi import HelloWorld
from app.apis.LoginApi import Login
from app.apis.MovieApi import MovieResource
from app.apis.PasswordApi import PasswordResource
from app.apis.RegisterApi import UserRegister
from app.apis.SmsApi import SMSResource
from app.apis.SmsLoginApi import SmsLogin

api = Api()

def init_api(app):
    api.init_app(app)


api.add_resource(HelloWorld, '/api/v1/hello/')
api.add_resource(CityResource, '/api/v1/city/') # 区域信息
api.add_resource(UserRegister, '/api/v1/register/') # 注册
api.add_resource(UserAcitve, '/api/v1/useractive/')  # 激活
api.add_resource(Login, '/api/v1/login/')   # 登录
api.add_resource(SMSResource, '/api/v1/sms/')   # 发短信
api.add_resource(SmsLogin, '/api/v1/smslogin/') # 手机短信登录
api.add_resource(PasswordResource, '/api/v1/password/') # 修改密码
api.add_resource(UploadHeadFile, '/api/v1/headimg/')    # 上传头像
api.add_resource(MovieResource, '/api/v1/movie/')   # 电影信息
api.add_resource(CinemasResource, '/api/v1/cinema/')    # 影院信息
