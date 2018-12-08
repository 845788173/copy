from flask import Blueprint, request, abort

blue=Blueprint('first_blue',__name__,url_prefix='/blue/')



@blue.route('/index/')
def index():
    return 'helloflask'
# @blue.route('/addperson/')
# def add_person():
#     person=Person()
#     flag=random.randrange(100)
#     person.p_name='爱学习的小明%d'%flag
#     person.p_age=flag
#     db.session.add(person)
#     db.session.commit()
#
#     return 'add success'
#
# @blue.route('/getpersons/')
# def get_persons():
#     persons=Person.query.all()
#     return render_template('personlist.html',persons=persons)
#
# @blue.route('/getperson/')
# def get_person():
#     # person=Person.query.get(1)
#     person=Person.query.order_by('-id').first()
#     print(person)
#     return '发现person'
#
# @blue.route('/getpersonswithpage/')
# def get_persons_with_page():
#     #获取数据
#     #获取第几页的数据
#     #每一页获取多少条数据
#     page=request.args.get('page',1,type=int)
#     per_page=request.args.get('per_page',3,type=int)
#     persons=Person.query.limit(per_page).offset((page-1)*per_page)
#     return render_template('personlist.html', persons=persons)
# @blue.route('/getpersonsbypaginate/')
# def get_persons_by_paginate():
#     page = request.args.get('page', 1, type=int)
#     per_page = request.args.get('per_page', 3, type=int)
#     paginations=Person.query.paginate(page,per_page)
#
#     return render_template('bootstrap.html', paginations=paginations)
#
# @blue.route('/addgrade/')
# def add_grade():
#     grade=Grade()
#     grade.g_name='python%d'% random.randrange(10000)
#     db.session.add(grade)
#     db.session.commit()
#     return 'add success'
#
# @blue.route('/addstudent/')
# def add_student():
#     grade=Grade.query.order_by('-id').first()
#     student=Student()
#     student.s_name='好承训员%d'% random.randrange(100)
#     student.s_grade_id=grade.id
#     db.session.add(student)
#     db.session.commit()
#     return 'add success'
#
# @blue.route('/getgradebystudent/')
# def get_grade_by_student():
#     student=Student.query.order_by('-id').first()
#     grade=Grade.query.get(student.s_grade_id)
#     print(grade)
#     grade=student.grade
#     return '班级%s'% grade.g_name
#
# @blue.route('/getstudentsbygrade/')
# def get_students_by_grade():
#     grade=Grade.query.order_by('-id').first()
#     # students=Student.query.filter(Student.s_grade_id==grade.id)
#     print(grade.g_students)
#     students=grade.g_students
#     return render_template('studentlist.html', students=students)
@blue.before_request
def process_request():
    print('请求之前')
    print(request.path)
    print(request.remote_addr)
    if request.path=='/index/':
        return  '本网站不欢迎你'

@blue.route('/bug/')

def bug():
    abort(401)
    return 'make401'


@blue.errorhandler(401)
def process_exception(e):
    print(e)
    return '小伙子你的程序有bug'