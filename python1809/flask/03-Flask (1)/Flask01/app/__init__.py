import os

from flask import Flask
from flask_migrate import Migrate

from app.models import db
from app.views import blue


def create_app():
    app = Flask(__name__)


    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    ########### sqlite
    # 在使用 db.create_all() 时，数据库是没有问题
    # 在使用migrate操作时，文件就会出现偏差。配置和实际不匹配 【因为是相对路径】
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

    # 根目录
    # /home/atom/Desktop/Flask1809/03-Flask/Flask01/app
    # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(BASE_DIR, 'test.db')
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(BASE_DIR, '../test.db')

    ########### mysql
    # 前提安装有驱动: pymysql
    # 前提连接的数据库 已存在!!!
    # dialect + driver: // username: password @ host:port / database
    # 数据库+驱动://数据库用户名:数据库密码@主机:端口号/需要连接的数据库
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/szpython18091115'


    app.register_blueprint(blueprint=blue)

    db.init_app(app)


    # flask-migrate 【数据库表单迁移】    结合    flask-script 【需要在Manager实例后，关联】
    migrate = Migrate(app=app, db=db)

    return app