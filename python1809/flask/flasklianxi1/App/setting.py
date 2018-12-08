from flask import config


def get_db_uri(database):
    ENGINE=database.get('ENGINE') or 'mysql'
    DRIVER=database.get('DRIVER') or 'pymysql'
    USERNAME=database.get('USERNAME') or 'root'
    PASSWORD=database.get('PASSWORD') or '7986805'
    HOST=database.get('HOST') or 'localhost'
    PORT=database.get('PORT') or '3306'
    NAME=database.get('NAME') or 'python1809'
    return '{}+{}://{}:{}@{}:{}/{}'.format(ENGINE,DRIVER,USERNAME,PASSWORD,HOST,PORT,NAME)


class Baseconfig():
    DEBUG=False
    SECRET_KEY='frgfbvkhfsvlkuvlf'
    TESTING=False
    SQLALCHEMY_TRACK_MODIFICATIONS=False



class Developmentconfig(Baseconfig):
    DEBUG = True
    DATABASE={
        'ENGINE':'mysql',
        'DRIVER': 'pymysql',
        'USERNAME': 'root',
        'PASSWORD': '7986805',
        'HOST' :'127.0.0.1',
        'PORT': '3306',
        'NAME':'python1809',
    }



    SQLALCHEMY_DATABASE_URI=get_db_uri(DATABASE)


class Testingconfig(Baseconfig):
    TESTING = True
    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USERNAME': 'root',
        'PASSWORD': '7986805',
        'HOST': '127.0.0.1',
        'PORT':'3306',
        'NAME': 'python1809',
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class Stagingconfig(Baseconfig):

    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USERNAME': 'root',
        'PASSWORD': '7986805',
        'HOST': '127.0.0.1',
        'PORT':'3306',
        'NAME': 'python1809',
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class Productconfig(Baseconfig):

    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USERNAME': 'root',
        'PASSWORD': '7986805',
        'HOST': '127.0.0.1',
        'PORT':'3306',
        'NAME': 'python1809',
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

envs={
    'Develop':Developmentconfig,
    'Testing':Testingconfig,
    'Staging':Stagingconfig,
    'Product':Productconfig,
}

def init_app(app,env_name):
    app.config.from_object(config.get(env_name))




