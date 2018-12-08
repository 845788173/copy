import random

from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
from App.models import User


# 首页
def index(request):
    result_list = random.sample(range(1,76), 67)
    print(result_list)

    # 获取cookie
    username = request.COOKIES.get('username')

    return render(request, 'index.html', context={'username':username})


 # 项目抽取
def randomview(request):
    result_list = [17, 62, 54, 25, 57, 11, 12, 30, 56, 23, 43, 71, 4, 7, 58, 29, 28, 13, 70, 35, 72, 18, 53, 37, 45, 41, 46, 14, 39, 15, 50, 64, 21, 75, 48, 74, 5, 60, 67, 66, 20, 16, 73, 65, 47, 24, 44, 10, 59, 33, 36, 42, 69, 9, 68, 26, 34, 6, 2, 27, 3, 8, 55, 61, 63, 40, 51]
    # print(result_list.sort())

    return render(request, 'randomview.html', context={'result_list':result_list})


# 视图函数中，第一个参数都是request
def goods(request, num=1):

    str = '你需要的是第%s页商品数据' % num

    return HttpResponse(str)


# url参数和视图函数是对应的
def detail(request, a, b, c):
    return HttpResponse('测试')


def requesttest(request):

    data = {
        # 请求路径
        'path': request.path,

        # 请求方式
        'method': request.method,

        # GET请求参数
        # http://127.0.0.1:8000/requesttest/?name=zyz&age=18
        'getargs': request.GET,

        # POST请求参数
        'postargs': request.POST,

        # FILES文件
        # request.FILES

        # COOKIES
        # request.COOKIES

        # session
        # session
    }


    return render(request, 'requesttest.html', context=data)


# GET
def gettest(request):
    # 获取 客户端 传递的数据

    # 方式一: 字典操作，如果key不存在，会报错
    # name = request.GET['name']
    # age = request.GET['age']

    # 方式二： 通过get方法
    # 如果不存在，设置为None
    # 预设置默认值
    name = request.GET.get('name')
    age = request.GET.get('age')
    score = request.GET.get('score', 0)

    return HttpResponse('我叫: {}, 我今年{}岁, 我的考试成绩{}'.format(name,age,score))


# POST
def posttet(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    score = request.POST.get('score', 0)

    return HttpResponse('我叫: {}, 我今年{}岁, 我的考试成绩{}'.format(name, age, score))


def responsetest(request):
    # response = HttpResponse('hello')

    # response = render(request, 'responsetest.html')

    # response = HttpResponseRedirect('/')
    # response = HttpResponseRedirect('/randomview/')
    # response = redirect('/randomview/')

    # response = redirect('app:randomview')
    # response = redirect('app:goods', 13)
    # response = redirect('app:detail', 1,2,3)

    stu = {
        'name':'atom',
        'age':18,
        'sex':'男'
    }

    response = JsonResponse(stu)

    return response



##########################
# 注册
def register(request):
    if request.method == 'GET': # 获取注册页面
        return render(request, 'register.html')
    elif request.method == 'POST':  # 注册操作
        # 获取客户端传入的数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        tel = request.POST.get('tel')
        print(username,password,tel)

        # 存入数据库
        user = User()
        user.username = username
        user.password = password
        user.tel = tel
        user.save()

        # 重定向首页
        response = redirect('app:index')

        # 状态保持
        response.set_cookie('username', username)

        # return HttpResponse('注册成功')
        return response


# 退出
def logout(request):
    # 重定向首页
    response = redirect('app:index')

    # 删除cookie
    response.delete_cookie('username')

    return response

# 登录
def login(request):
    if request.method == 'GET': # 获取登录页面
        return render(request, 'login.html')
    elif request.method == 'POST':  # 登录操作
        # 获取数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)

        # 验证
        # 数据库能找到，登录成功
        # 数据库找不到，登录失败
        users = User.objects.filter(username=username).filter(password=password)
        if users.count():   # 存在
            user = users.first()

            # 重定向首页
            response = redirect('app:index')

            # 设置cookie
            response.set_cookie('username', user.username)

            return response

        else:   # 不存在
            return HttpResponse('用户名或密码错误!')


        # return HttpResponse('登录成功')


def cart(request):

    username = request.COOKIES.get('username')

    # 获取对应用户的购物车列表

    return render(request, 'cart.html', context={'username':username})