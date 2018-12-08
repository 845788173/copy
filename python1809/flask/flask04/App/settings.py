



def get_db_uri(dbinfo):
    ENGINE=dbinfo.get('ENGINE')or 'mysql'
    DRIVER=dbinfo.get('DRIVER')or 'pymysql'
    USER=dbinfo.get('USER')or 'root'
    PASSWORD=dbinfo.get('PASSWORD')or '7986805'
    HOST=dbinfo.get('HOST')or 'localhost'
    PORT=dbinfo.get('PORT')or '3306'
    NAME=dbinfo.get('NAME')or 'python1804flaskday04'
    return '{}+{}://{}:{}@{}:{}/{}'.format(ENGINE,DRIVER,USER,PASSWORD,HOST,PORT,NAME)



class Config:
    DEBUG=False
    TESTING=False
    SECRET_KEY='lliang'
    SQLALCHEMY_TRACK_MODIFICATIONS=False




class DevelopConfig(Config):
    DEBUG = True
    DATABASE={
        'ENGINE':'mysql',
        'DRIVER':'pymysql',
        'USER':'root',
        'PASSWORD':'7986805',
        'HOST':'127.0.0.1',
        'PORT':'3306',
        'NAME':'python1804flaskday04'
    }
    SQLALCHEMY_DATABASE_URI= get_db_uri(DATABASE)


class TestingConfig(Config):
    TESTING = True
    DATABASE={
        'ENGINE':'mysql',
        'DRIVER':'pymysql',
        'USER':'root',
        'PASSWORD':'7986805',
        'HOST':'127.0.0.1',
        'PORT':'3306',
        'NAME':'python1804flaskday04'
    }
    SQLALCHEMY_DATABASE_URI= get_db_uri(DATABASE)


class StagingConfig(Config):

    DATABASE={
        'ENGINE':'mysql',
        'DRIVER':'pymysql',
        'USER':'root',
        'PASSWORD':'7986805',
        'HOST':'127.0.0.1',
        'PORT':'3306',
        'NAME':'python1804flaskday04'
    }
    SQLALCHEMY_DATABASE_URI= get_db_uri(DATABASE)

class ProductConfig(Config):

    DATABASE={
        'ENGINE':'mysql',
        'DRIVER':'pymysql',
        'USER':'root',
        'PASSWORD':'7986805',
        'HOST':'127.0.0.1',
        'PORT':'3306',
        'NAME':'python1804flaskday04'
    }
    SQLALCHEMY_DATABASE_URI= get_db_uri(DATABASE)

envs={
    'Develop':DevelopConfig,
    'Testing':TestingConfig,
    'Staging':StagingConfig,
    'Product':ProductConfig,
    'default':DevelopConfig,
}