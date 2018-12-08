


from flask import Flask

from App.apis import init_api
from App.ext import init_ext
from App.settings import init_app


def create_app(env_name='default'):

    app = Flask(__name__)
    init_app(app,env_name)
    init_ext(app)
    init_api(app)

    return app