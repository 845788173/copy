import random

from flask import Blueprint, render_template

from App.ext import db
from App.models import Student

blue=Blueprint('first',__name__)

def  init_blue(app):
    app.register_blueprint(blueprint=blue)

@blue.route('/')
def index():
    return 'Hello'

@blue.route('/addstudent/')
def add_student():
    student=Student()
    student.s_name='小hong'
    db.session.add(student)
    db.session.commit()
    return 'Create successful'
@blue.route('/getstudents/')
def get_students():
    students=Student.query.all()
    for student in students:
        print(student.s_name)
        return render_template('studentlist.html',students=students)

@blue.route('/addstudents/')
def add_students():
    students=[]

    for i in range(10):
        student=Student()
        student.s_name='aixue%d' % random.randrange(100)
        students.append(student)
        db.session.add_all(students)
        db.session.commit()
        return 'Add success'