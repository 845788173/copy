import random

from flask import Blueprint, abort, request, render_template, redirect, url_for, session

from App import db
from App.models import User

blue=Blueprint('firstblue',__name__)


@blue.route('/')
def index():
    username=session.get('username')
    return render_template('index.html',username=username)


@blue.route('/errorstatus/')
def error_status():
    abort(404)
    return 'success'

@blue.errorhandler(404)
def error_hander(exception):
    return exception
@blue.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    elif request.method=='POST':
        username=request.form.get('username')

        response=redirect(url_for('firstblue.index'))
        session['username']=username
        return response
@blue.route('/logout/')
def logout():
    response=redirect(url_for('firstblue.index'))
    # response.delete_cookie('username')
    session.pop('username')
    return response
@blue.route('/home/')
def home():
    name1=''
    name2=''
    name3=''
    data=[
        {
            'kjjh':'hhhhuh','hjs':3163561
        },
        {'hjfjsh':'jsjj','hsfcsfc':'hvffdz'},
    ]
    return render_template('index.html',name1=name1,name2=name2,data=data)
@blue.route('/createall/')
def create_all():
    db.create_all()
    return 'hjfsfjaj'
@blue.route('/dropall/')
def drop_all():
    db.drop_all()
    return 'success'
@blue.route('/adduser/')
def add_user():
    user=User()
    user.username=random.randrange(100)
    user.age=random.randrange(200)
    db.session.add(user)
    db.session.commit()
    return 'hsfsfjdagv'
@blue.route('/showuser/')
def show_user():
    users=User.query.all()
    return render_template('index.html', users=users)
