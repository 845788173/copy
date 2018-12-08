from flask import Blueprint

blue = Blueprint('blue', __name__)

@blue.route('/')
def hello_world():

    return '小伙别跑'


