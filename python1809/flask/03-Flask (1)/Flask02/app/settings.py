import os



# 根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# URI拼接
def get_db_uri(database):
    db = database.get('db') or 'mysql'
    driver = database.get('driver') or 'pymysql'
    username = database.get('username') or 'root'
    password = database.get('password') or '123456'
    host = database.get('host') or '127.0.0.1'
    port = database.get('port') or '3306'
    dbname = database.get('dbname') or 'sz01'

    return '{}+{}://{}:{}@{}:{}/{}'.format(db,driver,username,password,host,port,dbname)


# 基础类(公共配置)
class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = '%^&*(4567890,./DFGHJqweqwe'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# 开发环境
class DevelopConfig(BaseConfig):
    DEBUG = True
    # 数据库配置
    DATABASE = {
        'dbname': 'szpython18091115'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

# 测试环境
class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASE_DIR, 'testing.db')

# 演示环境
class StagingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASE_DIR, 'staging.db')

# 线上环境
class ProductConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASE_DIR, 'product.db')


config = {
    'develop': DevelopConfig,   # 开发环境
    'testing': TestingConfig,   # 测试环境
    'staging': StagingConfig,   # 演示环境
    'product': ProductConfig,   # 线上环境
    'default': DevelopConfig,   # 默认环境
}


def init_app(app, env_name):
    app.config.from_object(config.get(env_name))
