import os

from flask import Flask

from App.ext import  init_ext
from App.setting import init_app
from App.views import blue, init_blue


def create_app( env_name='Developmentconfig'):

    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    # BASE_DIR=os.path.dirname(os.path.abspath(__file__))

    # app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////'+os.path.join(BASE_DIR,'test.db')
    # app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////'+os.path.join(BASE_DIR,'../test.db')
    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:7986805@localhost:3306/python1809'
    init_app(app,env_name)
    # init_app(app.config.from_object(envs.get(env_name)))

    init_ext(app)
    init_blue(app)

    return app