def get_db_uri(dbinfo):
    ENGINE = dbinfo.get('ENGINE') or 'mysql'
    DRIVER = dbinfo.get('DRIVER') or 'pymysql'
    USER = dbinfo.get('USER') or 'root'
    PASSWORD = dbinfo.get('PASSWORD') or '7986805'
    HOST = dbinfo.get('HOST') or 'localhost'
    PORT = dbinfo.get('PORT') or '3306'
    NAME = dbinfo.get('NAME') or 'test'
    return '{}+{}://{}:{}@{}:{}/{}'.format(ENGINE, DRIVER, USER, PASSWORD, HOST, PORT, NAME)


class Config():
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'kyugkgkhjoddfgiiydersyygewaewaekjkpih'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DeveloConfig(Config):
    DEBUG = True
    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '7986805',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'python1804flaskproject'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class TestingConfig(Config):
    TESTING = True
    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '7986805',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'python1804flaskprojectTesting'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class StagingConfig(Config):
    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '7986805',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'python1804flaskprojectStaging'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class ProductConfig(Config):
    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '7986805',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'python1804flaskprojectProduct'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


envs = {
    'develop': DeveloConfig,
    "testing": TestingConfig,
    'staging': StagingConfig,
    'product': ProductConfig,
}