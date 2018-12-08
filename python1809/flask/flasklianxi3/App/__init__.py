

from flask import Flask

from App.ext import init_ext
from App.settings import init_app
from App.views import init_blue


def create_app(env_name='default'):
    app = Flask(__name__)
    init_app(app,env_name)
    init_blue(app)
    init_ext(app)

    return app