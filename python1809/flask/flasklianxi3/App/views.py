import os
import uuid

from flask import Blueprint, render_template, request, session, redirect, url_for

from App.models import *

blue=Blueprint('blue',__name__)


def init_blue(app):
    app.register_blueprint(blueprint=blue)


# @blue.route('/')
# def index():
#     wheels = [
#         {'name': '阿卡丽1', 'img': '/static/img/Akali_Splash_0.jpg'},
#         {'name': '阿卡丽2', 'img': '/static/img/Akali_Splash_1.jpg'},
#         {'name': '阿卡丽3', 'img': '/static/img/Akali_Splash_2.jpg'},
#         {'name': '阿卡丽4', 'img': '/static/img/Akali_Splash_3.jpg'},
#         {'name': '阿卡丽5', 'img': '/static/img/Akali_Splash_4.jpg'},
#
#     ]
#     goodlist=Goods.query.all()
#     return render_template('index.html',wheels=wheels,goodlist=goodlist)

# @blue.route('/')
# @blue.route('/<int:num>/<int:per>/')
# def index(num=1,per=6):
#     wheels=[
#         {'name': '阿卡丽1', 'img': '/static/img/Akali_Splash_0.jpg'},
#         {'name': '阿卡丽2', 'img': '/static/img/Akali_Splash_1.jpg'},
#         {'name': '阿卡丽3', 'img': '/static/img/Akali_Splash_2.jpg'},
#         {'name': '阿卡丽4', 'img': '/static/img/Akali_Splash_3.jpg'},
#         {'name': '阿卡丽5', 'img': '/static/img/Akali_Splash_4.jpg'},
#     ]
#     # goodlist=Goods.query.all()
#     goodlist=Goods.query.offset((num-1)*6).limit(per)
#     return render_template('index.html',goodlist=goodlist,wheels=wheels)

@blue.route('/')
@blue.route('/<int:num>/<int:per>/')
def index(num=1,per=6):
    wheels=[
        {'name': '阿卡丽1', 'img': '/static/img/Akali_Splash_0.jpg'},
        {'name': '阿卡丽2', 'img': '/static/img/Akali_Splash_1.jpg'},
        {'name': '阿卡丽3', 'img': '/static/img/Akali_Splash_2.jpg'},
        {'name': '阿卡丽4', 'img': '/static/img/Akali_Splash_3.jpg'},
        {'name': '阿卡丽5', 'img': '/static/img/Akali_Splash_4.jpg'},
    ]
    paginate=Goods.query.paginate(num,per)
    return render_template('index2.html',wheels=wheels,paginate=paginate)


@blue.route('/register/',methods=['POST'])
def register():
    user=User()
    user.name=request.form.get('username')
    user.password=request.form.get('password')
    user.email=request.form.get('email')
    user.token=str(uuid.uuid5(uuid.uuid4(),user.email))

    db.session.add(user)
    db.session.commit()
    session['token']='token'
    return redirect(url_for('blue.index'))

@blue.route('/login/',methods=['POST'])
def login():
    email=request.form.get('email')
    password=request.form.get('password')
    users=User.query.filter(User.email==email,User.password==password)
    print('###################################')
    print(users)
    if users.count():
        user=users.first()
        print(user)
        user.token=str(uuid.uuid5(uuid.uuid4(),email))
        db.session.add(user)
        db.session.commit()
        session['token']=user.token
        return redirect(url_for('blue.index'))
    else:
        return 'qingqiufangshicuowu'
@blue.route('/logout/')
def logout():
    session.pop('token')
    return redirect(url_for('blue.index'))

@blue.before_requst
def before():
    token=session.get['token']
    if token:
        user=User.query.filter(User.token==token).first()
    else:
        user=None

        g.user=user


















































