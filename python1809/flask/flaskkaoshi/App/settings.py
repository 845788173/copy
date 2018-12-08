import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# UPLOAD_RID = os.path.join(BASE_DIR, 'static/img/')


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY='jkdavkjanvdk'


class DevelopConfig(BaseConfig):
    # SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASE_DIR, 'develop.db')

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:7986805@127.0.0.1:3306/python07'

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
