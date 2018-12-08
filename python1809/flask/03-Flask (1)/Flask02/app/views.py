import random

from flask import Blueprint, render_template

from app.ext import db
from app.models import User, Grade, Student

blue = Blueprint('blue', __name__)

def init_blue(app):
    app.register_blueprint(blueprint=blue)

@blue.route('/')
def index():
    return render_template('index.html')

# 添加数据
@blue.route('/adduser/')
def adduser():
    user = User()
    user.name = 'Atom-' + str(random.randrange(100000))
    user.age = random.randrange(18, 30)
    user.tel = str(random.randrange(10000000000,99999999999))
    user.score = random.randrange(1,100)

    db.session.add(user)
    db.session.commit()

    return '添加用户: %s' % user.name


# 获取数据  【结果集】
@blue.route('/getusers/')
def getusers():
    # 获取所有数据
    # users = User.query.all()

    # 比较
    # users = User.query.filter(User.age >= 25)
    # users = User.query.filter(User.id == 3)
    # users = User.query.filter(User.age >=25).filter(User.score < 60)

    # 以xx开头
    # users = User.query.filter(User.score.startswith('9'))

    # 以xx结尾
    # users = User.query.filter(User.score.endswith('8'))

    # 包含xx
    # users = User.query.filter(User.tel.contains('8'))

    # 在...内
    # users = User.query.filter(User.id.in_([1,2,3,4,5]))

    # 模糊查询
    # users = User.query.filter(User.name.like('%3%'))

    # 限制个数
    # users = User.query.filter(User.name.like('%3%')).limit(3)
    # users = User.query.limit(5)

    # 排序
    # users = User.query.order_by(-User.score)

    # 偏移
    # users = User.query.offset(3)

    # 分页
    # users = User.query.limit(5)
    # users = User.query.offset(10).limit(5)

    # 注意  [limit最后才是执行]
    # users = User.query.order_by(-User.id).offset(3).limit(3)
    users = User.query.order_by(-User.id).limit(3).offset(3)

    return render_template('getusers.html', users=users)

# 获取数据 【单个数据】
@blue.route('/getuser/')
def getuser():

    # 通过主键获取数据
    # user = User.query.get(3)

    # 获取第一行数据
    # user = User.query.first()

    # 不能用
    # user = User.query.last()

    user = User.query.order_by(-User.id).first()

    return render_template('getuser.html', user=user)




#################### 级联数据
@blue.route('/addgrade/')
def addgrad():
    grade = Grade()
    grade.g_name = 'Python18' + str(random.randrange(10,100))

    db.session.add(grade)
    db.session.commit()

    return '添加班级成功: %s' % grade.g_name


@blue.route('/showgrade/')
def showgrade():

    grades = Grade.query.all()

    return render_template('showgrade.html', grades=grades)


@blue.route('/addstudent/')
def addstudent():
    stu = Student()
    stu.s_name = '张三%d号' % random.randrange(100000)
    stu.s_score = random.randrange(1,100)
    stu.s_age = random.randrange(18,30)

    # 哪个班级?
    grade = Grade.query.order_by(-Grade.id).first()
    stu.s_grade = grade.id

    db.session.add(stu)
    db.session.commit()

    return '添加学生成功:%s' % stu.s_name


@blue.route('/showstudent/')
def showstudent():
    students = Student.query.all()
    return render_template('showstudent.html', students=students, title='所有学生')


@blue.route('/showstudent/<int:gradeid>/')
def showGradeStudents(gradeid):
    ## 获取对应班级的学生信息

    # 方式一: 直接过滤
    # students = Student.query.filter(Student.s_grade == gradeid)
    # title = '%d班级' % gradeid
    # return render_template('showstudent.html',students=students, title=title)

    # 方式二: 级联
    grade = Grade.query.get(gradeid)

    return render_template('showstudent.html', students=grade.g_students, title=grade.g_name)