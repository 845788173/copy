from flask import Flask
from app.ext import init_ext
from app.settings import init_app
from app.views import init_blue


def create_app(env_name='default'):
    app = Flask(__name__)

    # 配置 settings.py
    init_app(app,env_name)

    # 插件 ext.py
    init_ext(app)

    # 蓝图 views.py
    init_blue(app)

    return app