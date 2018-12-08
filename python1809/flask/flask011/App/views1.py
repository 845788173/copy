from flask import Blueprint, render_template, request, redirect, url_for, flash

from App.views import blue

blue=Blueprint('second',__name__)
@blue.route('/index/')
def index():
    return render_template('index.html')




@blue.route('/mine/')
def mine():
    return render_template('mine.html')

@blue.route('/hellobs/')
def hellobs():
    return render_template('hello-bootstrap.html')

@blue.route('/userlogin/' ,methods=['GET','POST'])
def user_login():
    if request.method=='GET':
        return render_template('urerlogin.html')

    elif request.method=='POST':
        flash('用户名或密码错误')
        return redirect(url_for('second.user_login'))

