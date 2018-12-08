import os

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
class Config():
    DEBUG=False
    TESTING=False
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class Develop(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI='sqlite:////'+os.path.join(BASE_DIR,'test.db')
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:7986805@localhost:3306/python05'


envs={
    'Develop':Develop,
    'default':Develop,
}
def init_app(app,env_name):
    app.config.from_object(envs.get(env_name))