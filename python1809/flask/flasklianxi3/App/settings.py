import os

BASE_DIR=os.path.dirname(os.path.abspath(__file__))

def get_db_uri(database):
    db=database.get('db')or 'mysql'
    driver=database.get('driver') or 'pymysql'
    username=database.get('username') or 'root'
    password=database.get('password') or '7986805'
    host=database.get('host') or '127.0.0.1'
    port=database.get('port') or '3306'
    name=database.get('name') or 'python1804'

    return '{}+{}://{}:{}@{}:{}/{}'.format(db,driver,username,password,host,port,name)


class Config():
    DEBUG:False
    TESTING=False
    SECRET_KEY='jgdvdihuglithg'

    SQLALCHEMY_TRACK_MODIFICATIONS=False

class Developconfig(Config):
    DEBUG = True
    DATABASE={
        'db': 'mysql',
        'driver':'pymysql',
        'username':'root',
        'password':'7986805',
        'host':'localhost',
        'port':'3306',
        'name':'python1804',


    }
    SQLALCHEMY_DATABASE_URI =get_db_uri(DATABASE)

envs={
    'develop':Developconfig,
    'default':Developconfig,
}

def init_app(app,env_name):
    app.config.from_object(envs.get(env_name))