import random

from django.http import HttpResponse
from django.shortcuts import render
from App.models import Dog, Person, IDCard, Grade, Student, User, Goods


# Create your views here.
def index(request):
    return render(request, 'index.html')


# 添加狗
def adddog(request):
    # dog = Dog()
    # dog.d_name = '旺财-' + str(random.randrange(100000))
    # dog.d_color = '#' + str(random.randrange(100, 100000))
    # dog.d_age = random.randrange(0, 18)

    dog = Dog.createDog('旺财-' + str(random.randrange(100000)), '#' + str(random.randrange(100, 100000)), random.randrange(0, 18))

    dog.save()

    return HttpResponse('你家狗狗新成员:' + dog.d_name)

# 显示狗
def showdog(request):
    # 所有数据
    # dogs = Dog.objects.all()

    # 删除，不显示
    # dogs = Dog.objects.filter(isdelete=False)

    # 为了后续操作方便，自定义管理器 【删除的数据过滤】
    dogs = Dog.myobjects.all()

    str = ''
    for dog in dogs:
        str += '<p> {}-{}  {}</p>'.format(dog.id, dog.d_name, dog.d_age)

    return HttpResponse(str)



############### 一对一 ###############
# 添加人
def addperson(request):
    per = Person()
    per.p_name = '阿童木-' + str(random.randrange(10000000))
    per.p_age = random.randrange(10,100000)
    per.save()

    return HttpResponse('{}已满16岁!'.format(per.p_name))

# 添加身份证
def addcard(request):
    idcard = IDCard()
    idcard.i_num = '441622{}{}{}1234'.format(random.randrange(2000,2020), random.randrange(1,13), random.randrange(1,30))
    idcard.i_addr = '深圳市南山区大学城 创客小镇 16栋 3楼Python1809 {}号'.format(random.randrange(1,70))

    # 身份证 绑定 人
    per = Person.objects.last()
    idcard.i_person = per

    idcard.save()

    return HttpResponse('身份证号: {} -- 绑定名: {}'.format(idcard.i_num, per.p_name))


# 杀死某人
def delperson(request):
    per = Person.objects.last()
    per.delete()

    return HttpResponse('某某人已经被杀死了!')

# 获取人对应的身份证
def getpersoncard(request):

    # 人 主表
    # 身份证 从表
    # 主表 获取 从表 【隐性】
    per = Person.objects.last()

    # IDCard 模型类  -->  表 idcard
    idcard = per.idcard

    return HttpResponse('身份证号: {} -- 绑定名: {}'.format(idcard.i_num, per.p_name))

# 获取身份证对应人的信息
def getcardperson(request):

    card = IDCard.objects.last()

    # 从表 获取 主表， 关系属性
    per = card.i_person

    return HttpResponse('姓名:{}, 年龄:{}'.format(per.p_name, per.p_age))



############### 一对多 ###############
def addgrade(request):
    grade = Grade()
    grade.g_name = 'python18' + str(random.randrange(10,100))
    grade.save()

    return HttpResponse('添加 {} 班级成功!'.format(grade.g_name))

def addstudent(request):
    stu = Student()
    stu.s_name = 'Atom' + str(random.randrange(1000))
    stu.s_score = random.randrange(1,100)

    # 添加到最后一个班级
    grade = Grade.objects.last()
    stu.s_grade = grade

    stu.save()

    return HttpResponse('{} 学生成功成功!'.format(stu.s_name))


def delgrade(request):
    grade = Grade.objects.last()
    grade.delete()

    return HttpResponse('删除班级成功!')


def showgrade(request):
    # 班级
    grade_list = Grade.objects.all()

    info = ''
    for grade in grade_list:
        # 获取班级 对应 学生信息 [隐性]
        # student_set ===> objects
        student_list = grade.student_set.all()

        student_str = ''
        for student in student_list:
            student_str += '<i> {} </i>'.format(student.s_name)

        info += '<p> 班级: {} 班级人数:{}  人员列表:{} </p>'.format(grade.g_name, student_list.count(), student_str)

    return HttpResponse(info)


def showstudent(request):
    students = Student.objects.all()

    student_str = ''
    for student in students:
        # 获取 学生 对应 班级 [显性]
        grade = student.s_grade

        student_str += '<p> 姓名:{} 成绩:{}  班级:{}</p>'.format(student.s_name, student.s_score, grade.g_name)

    return HttpResponse(student_str)


############### 多对多 ###############
def adduser(request):
    user = User()
    user.u_name = '明智-' + str(random.randrange(1000))
    user.u_tel = random.randrange(10000000000,99999999999)
    user.save()

    return HttpResponse('用户 {} 注册成功!'.format(user.u_name))


def addgoods(request):
    goods = Goods()
    goods.g_name = 'ipad-' + str(random.randrange(1,10))
    goods.g_price = random.randrange(1000,20000)
    goods.save()

    return HttpResponse('添加商品 {} 成功'.format(goods.g_name))


def addcart(request):
    user = User.objects.last()
    goods = Goods.objects.last()

    # 关系
    goods.g_user.add(user)
    goods.save()

    return HttpResponse('{} 添加 {} 到购物车成功'.format(user.u_name,goods.g_name))


def showcart(request):
    # 一个用户 对应 多个商品
    user = User.objects.last()
    goods_list = user.goods_set.all()

    str = '<h1> {} 购物车 </h1>'.format(user.u_name)
    for goods in goods_list:
        str += '<p> 商品名称: {}    商品价格:{} </p>'.format(goods.g_name, goods.g_price)

    return HttpResponse(str)


def addcollect(request):
    goods = Goods.objects.last()
    user = User.objects.last()

    # 关系
    goods.g_user.add(user)
    goods.save()

    return HttpResponse('{} 被 {} 收藏!'.format(goods.g_name, user.u_name))


def showgoods(request):
    goods_list = Goods.objects.all()

    str = '<h1>商品列表</h1>'
    for goods in goods_list:

        # 一个商品 对应 多个用户
        user_list = goods.g_user.all()
        if user_list.count():
            str += '<p> 商品名称:{}   商品价格:{}   收藏数量:{}</p>  '.format(goods.g_name, goods.g_price, user_list.count())
        else:
            str += '<p> 商品名称:{}   商品价格:{} </p>'.format(goods.g_name, goods.g_price)

    return HttpResponse(str)