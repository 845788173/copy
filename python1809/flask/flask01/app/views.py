import random

from flask import Blueprint

blue = Blueprint('blue', __name__)

def init_blue(app):
    app.register_blueprint(blueprint=blue)

@blue.route('/')
def hello_world():
    temp = random.randrange(1,68)
    return '今天又是谁？ 我大名叫: %s' % temp