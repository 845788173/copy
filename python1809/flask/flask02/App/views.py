import random

from flask import Blueprint, render_template

from App.models import Person,db



blue=Blueprint('first',__name__)

@blue.route('/')
def index():
    return 'helloflask'

@blue.route('/createdb/')
def create_db():
    db.create_all()

    return 'DB Create success'

@blue.route('/addperson/')
def add_person():
    p=Person()
    p.p_name='谁着了拉出去枪毙%d'% random.randrange(100)
    db.session.add(p)
    db.session.commit()
    return 'Person Add Success'

@blue.route('/getpersons/')
def get_persons():
    persons=Person.query.all()
    # for person in persons:
        # print(person.p_name)
    return render_template('personlist.html',persons=persons)
