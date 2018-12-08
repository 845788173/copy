from flask import Flask

from App.models import db
from App.views import blue


def create_app():

    app = Flask(__name__,template_folder='../templates')
    app.register_blueprint(blueprint=blue)
    app.config['SECRET_KEY']='sgtsrhystjsfrhdhe'
    #test.db是相对于App下的路径
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
    db.init_app(app=app)
    return app