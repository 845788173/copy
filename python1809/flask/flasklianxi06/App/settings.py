


import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))



class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASE_DIR, 'develop.db')

    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/szpython1809tpp'

    # 邮箱配置
    # MAIL_SERVER = 'smtp.163.com'
    # MAIL_USERNAME = '18924235915@163.com'
    # MAIL_PASSWORD = 'zyz123'
    # MAIL_DEFAULT_SENDER = '18924235915@163.com'


config = {
    'develop': DevelopConfig,
    'default': DevelopConfig
}

def init_app(app, env_name):
    app.config.from_object(config.get(env_name))
