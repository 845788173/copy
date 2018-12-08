from flask import Flask

from App.ext import init_ext
from App.settings import envs
from App.views import init_blue


def create_app(env):
    #初始化app
    app=Flask(__name__,template_folder='../templates')
    #初始化配置这里的env是关键字有意义的
    app.config.from_object(envs.get(env))
    #初始化蓝图，路由,调用，注册
    init_blue(app)
    #初始化第三方库
    init_ext(app)

    return app