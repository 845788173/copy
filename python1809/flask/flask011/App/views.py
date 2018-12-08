from flask import app, make_response, Blueprint, url_for, render_template, request, Response, redirect, session

blue=Blueprint('first',__name__)

@blue.route('/response/')

def index():

    return 'index'

@blue.route('/url_for/')
def url():
    result=url_for('second.index')
    return result


@blue.route('/home/')
def home():
    # username=request.cookies.get('user')
    username=session.get('user')
    return render_template('home.html',username=username)

@blue.route('/login/',methods=['GET','POST'])
def login():
    if request.method=="GET":
        return render_template('login.html')
    elif request.method=="POST":
        username=request.form.get('username')
        session['user'] = username
        resp=Response(response='登入成功%s'%username)
        # resp.set_cookie('user',username)


        return resp
@blue.route('/logout/')
def logout():
    resp=redirect(url_for('first.home'))
    print(resp)
    resp.delete_cookie('user')

    return resp
