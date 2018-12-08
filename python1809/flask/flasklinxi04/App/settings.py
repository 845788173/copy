import os

BASE_DIR=os.path.dirname(os.path.abspath(__file__))

class Baseconfig():
    DEBUG=False
    TESTING=False
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class Developconfig(Baseconfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI='sqlite:////'+os.path.join(BASE_DIR,'develop.db')

envs={
    'Developconfig':Developconfig,
    'default':Developconfig,
}

def init_app(app,env_name):
    app.config.from_object(envs.get(env_name))

