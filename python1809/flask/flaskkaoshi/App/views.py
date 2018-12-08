from flask import Blueprint, render_template, request, redirect, url_for, jsonify, session

from App.models import *
from App.tools import get_token

blue=Blueprint('blue',__name__)


def init_blue(app):
    app.register_blueprint(blueprint=blue)

# @blue.route('/home/',methods=['GET'])
# def home():
#
#     token=session.get('token')
#     user=User.query.filter(User.token==token).first()
#     username=user.username
#     lunbos=Lunbo.query.all()
#     return render_template('home.html',lunbos=lunbos,username=username)



# @blue.route('/register/',methods=['POST','GET'])
# def register():
#     if request.method=='GET':
#         return render_template('register.html')
#     elif request.method=='POST':
#         user=User()
#         user.username=request.form.get('username')
#         user.password=request.form.get('password')
#         user.email=request.form.get('email')
#         user.token=get_token()
#         session['token']=user.token
#         db.session.add(user)
#         db.session.commit()
#         return redirect(url_for('blue.home'))
#
# @blue.route('/login/',methods=['GET','POST'])
# def login():
#     if request.method=='GET':
#         return render_template('login.html')
#     elif request.method=='POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         users = User.query.filter(User.username == username).filter(User.password==password)
#
#         if users.count()>0:
#             user=users.first()
#             user.token=get_token()
#             session['token']=user.token
#             db.session.add(user)
#             db.session.commit()
#             return redirect(url_for('blue.home'))
#         else:
#             return redirect(url_for('blue.login'))
#     else:
#         return '请求方式不对'
#
# @blue.route('/userinfo/',methods=['GET','POST'])
# def userinfo():
#     if request.method=='GET':
#         return render_template('userinfo_mod.html')
#     elif request.method=='POST':
#         username=request.form.get('username')
#         email=request.form.get('email')
#         user=User.query.filter(User.username==username).first()
#         user.email=email
#         user.token=get_token()
#         db.session.add(user)
#         db.session.commit()
#
#         return redirect(url_for('blue.home'))
#     else:
#         return '请求方式不对'
#
# @blue.route('/home_logined/')
# def home_logined():
#     return render_template('home_logined.html')




