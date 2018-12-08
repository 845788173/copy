import random

from django.http import HttpResponse
from django.shortcuts import render
from .models import *



def index(request):
    return render(request, 'index/index.html')

def adddog(request):
    dog=Dog()
    dog.d_name='旺财'+str(random.randrange(100))
    dog.d_color='#'+str(random.randrange(100))
    dog.d_age=random.randrange(10)
    dog.save()
    return HttpResponse('你家的小狗狗'+dog.d_name)

def addcard(request):
    idcard=IDCard()
    idcard.i_num=50
    idcard.i_addr='adsa'

    per=Person.objects.last()
    idcard.i_person=per
    idcard.save()
    return HttpResponse(idcard.i_addr)


# ############### 一对多 ###############
# def addgrade(request):
#     grade = Grade()
#     grade.g_name = 'python18' + str(random.randrange(10,100))
#     grade.save()
#
#     return HttpResponse('添加 {} 班级成功!'.format(grade.g_name))
#
# def addstudent(request):
#     stu = Student()
#     stu.s_name = 'Atom' + str(random.randrange(1000))
#     stu.s_score = random.randrange(1,100)
#
#     # 添加到最后一个班级
#     grade = Grade.objects.last()
#     stu.s_grade = grade
#
#     stu.save()
#
#     return HttpResponse('{} 学生成功成功!'.format(stu.s_name))
#
#
# def delgrade(request):
#     grade = Grade.objects.last()
#     grade.delete()
#
#     return HttpResponse('删除班级成功!')
#
#
# def showgrade(request):
#     # 班级
#     grade_list = Grade.objects.all()
#
#     info = ''
#     for grade in grade_list:
#         # 获取班级 对应 学生信息 [隐性]
#         # student_set ===> objects
#         student_list = grade.student_set.all()
#
#         student_str = ''
#         for student in student_list:
#             student_str += '<i> {} </i>'.format(student.s_name)
#
#         info += '<p> 班级: {} 班级人数:{}  人员列表:{} </p>'.format(grade.g_name, student_list.count(), student_str)
#
#     return HttpResponse(info)
#
#
# def showstudent(request):
#     students = Student.objects.all()
#
#     student_str = ''
#     for student in students:
#         # 获取 学生 对应 班级 [显性]
#         grade = student.s_grade
#
#         student_str += '<p> 姓名:{} 成绩:{}  班级:{}</p>'.format(student.s_name, student.s_score, grade.g_name)
#
#     return HttpResponse(student_str)

def addclass1(request):
    class1=Class1()
    class1.p_name='爱学习的小明%d'%random.randrange(100)


def student(request):
    students=Student.objects.all()
    class1=Class1.objects.all()
    students.s_class1=class1
    students.save()
    return HttpResponse('{},wo zmy'.format(students.))

def showgrade(request):
    grade_list=Grade.objects.all()
    for grade in grade_list:
        grade1=grade.leiming_set.all()


        student.
