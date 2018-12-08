import random

from flask import Blueprint, render_template

from App.models import *

blue=Blueprint('blue',__name__)
def init_blue(app):
    app.register_blueprint(blueprint=blue)

@blue.route('/')
def index():
    return render_template('index.html')


@blue.route('/adduser/')
def add_user():
    user=User()
    user.name = 'Atom-' +str(random.randrange(1000))
    user.age = random.randrange(18, 30)
    user.tel = str(random.randrange(10000000000, 99999999999))
    user.score = random.randrange(1, 100)
    db.session.add(user)
    db.session.commit()

    return 'success'

@blue.route('/getusers/')
def get_users():
    # users=User.query.all()
    # users=User.query.filter(User.age>15).filter(User.age<6)
    # users=User.query.filter(User.score.startswith('8'))
    # users=User.query.filter(User.score.endswith('9'))
    # users=User.query.filter(User.score.contains('8'))
    # users=User.query.filter(User.score.in_([1,2,3,4]))
    # users=User.query.filter(User.score.like(%3%)).limit(4)
    # users=User.query.order_by(-User.score)
    # users=User.query.offset(4)
    return render_template('getusers.html')

@blue.route('/getuser/')
def get_user():
    # user=User.query.get(id)
    # user=User.query.first()
    user=User.query.order_by(-User.score).first()
    return render_template('getuser.html',user=user)

@blue.route('/addgrade/')
def add_grade():
    grade=Grade()
    grade.g_name= grade.g_name = 'Python18' + str(random.randrange(10,100))
    db.session.add(grade)
    db.session.commit()
    return '%s' %grade.g_name

@blue.route('/showgrade/')
def show_grade():
    grade=Grade.query.all()
    return render_template('showgrade',grade=grade)

@blue.route('/addstudent/')
def add_student():
    stu = Student()
    stu.s_name = '%d'%random.randrange(1,1000)
    stu.s_score = random.randrange(1, 100)
    stu.s_age = random.randrange(18, 30)
    db.session.add(stu)
    db.session.commit()
    return 'success'

@blue.route('/showstudent/')
def show_student():
    students=Student.query.all()
    return render_template('showstudent.html',students=students,title='bhsgfsrf')
@blue.route('/showstudent/<int:gradeid>/')
def show_grade_student(gradeid):
    # students=Student.query.filter(Student.s_grade==gradeid)
    # title='%dbanji'%gradeid
    # return render_template('showstudent',students=students,title=title)
    grade=Grade.query.get(gradeid)
    return render_template('showstudent.html',students=grade.g_students,name=grade.g_name)








