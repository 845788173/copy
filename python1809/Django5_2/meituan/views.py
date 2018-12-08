from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from PIL import Image,ImageDraw,ImageFont
import io
import random

# Create your views here.
from meituan.models import User

def verifycode(request):
    # 图片基本设置
    # RGB: 0~255
    bgcolor = (random.randint(10, 200), random.randint(10,200), random.randint(10,200))
    # bgcolor = (120,120,120)
    width = 100
    height = 50

    # 创建图片
    image = Image.new('RGB', (width, height), bgcolor)

    # 画笔对象
    draw = ImageDraw.Draw(image)

    # 添加噪点
    for i in range(0,1000):
        # 坐标
        xy = (random.randint(0,width), random.randint(0,height))
        # 颜色
        fill = (random.randint(0,255), 255, random.randint(0,255))
        draw.point(xy, fill=fill)

    # 添加验证码
    str = '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'

    # 产生随机数
    rand_str = ''
    for i in range(0,4):
        rand_str += str[random.randint(0, len(str)-1)]
    print(rand_str)

    # 保存验证码

    # 指定字体类型
    font = ImageFont.truetype('static/fonts/Songti.ttc', 35)

    # 字体颜色
    font_color1 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    font_color2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    font_color3 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    font_color4 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # 绘制字体
    draw.text((5, 2),  rand_str[0], font=font, fill=font_color1)
    draw.text((25, 2), rand_str[1], font=font, fill=font_color2)
    draw.text((45, 2), rand_str[2], font=font, fill=font_color3)
    draw.text((65, 2), rand_str[3], font=font, fill=font_color4)

    # 释放画笔
    del draw

    # 文件操作
    buff = io.BytesIO()
    image.save(buff, 'png')


    return HttpResponse(buff.getvalue(), 'image/png')


def args01(request, a):

    return HttpResponse('传递的参数: ' + a)


def args02(request, a, b):

    return HttpResponse('传递的参数a={}, b={}'.format(a, b))


def test01(request):
    grade = Grade()

    return None


# 系统自动创建的
# 服务器接受到请求后，会自动根据报文创建HttpRequest对象
# GET请求: 请求参数放置在url后面，以?分割，参数与参数之间以&分割
# 例如： http://127.0.0.1:8000/meituan/?name=zhangsan&age=20&score=90
# https  ://  cn.bing.com  /search    ?  q=django  &  pc=MOZI  &  form=MOZLBR
def testrequest(request):
    # 请求完整路径
    print(request.path)

    # 请求方法 (HTTP方法)
    print(request.method)

    # GET请求参数 [类字典]
    print(request.GET)

    # POST请求参数 [类字段]
    print( request.POST )

    # 文件参数
    print(request.FILES)

    # cookie
    print(request.COOKIES)

    # session
    print(request.session)

    # 响应对象
    return HttpResponse('请求对象request')


def testget(request):
    # 获取客户端传递给服务器数据
    # 如果参数不存在，返回Nono
    username = request.GET.get('haha')
    # 不建议使用方括号的形式获取数据，参数如果不存在，会异常
    # score = request.GET['score']
    # score = request.GET.get('score')

    # get方法: 获取一个
    # getlist方法： 获取多个
    score = request.GET.getlist('score')

    print(username)
    print(score)

    return render(request, 'testget.html')


def testpost(request):
    username = request.POST.get('username')
    print(username)

    return render(request ,'testpost.html')


# HttpResonse对象: 返回数据给客户端
# 自己创建
def testresponse(request):
    # 直接返回
    response = HttpResponse('hello')

    # 带模板
    # response = render(request, 'response.html')

    # content 返回内容
    # status 状态码
    # 2xx 成功类
    # 3xx 重定向
    # 4xx 客户端错误
    # 5xx 服务器错误
    # response = HttpResponse('hello', status=404)

    # 重定向
    # response = redirect('/meituan/verifycode/')


    # 设置 set_cookie(key,value)
    response.set_cookie('name', 'atom')

    return response


def testjson(request):
    stu = {
        'name':'张三',
        'age':18,
        'score':90
    }

    # 获取 get_cookie(key)
    name = request.COOKIES.get('name')
    print(name)


    response = JsonResponse(stu)

    return response





# 首页
def index(request):
    # 获取cookie
    username = request.COOKIES.get('username')

    return render(request, 'index.html', context={'username':username})




# 注册
def register(request):
    if request.method == 'POST': # 注册操作
        # 获取客户端传递的数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        tel = request.POST.get('tel')

        # 保存到数据库
        user = User()
        user.u_name = username
        user.u_password = password
        user.u_tel = tel
        user.save()


        # 注册成功，直接重定向 首页
        response = redirect('/meituan/')

        # 设置cookie
        response.set_cookie('username', user.u_name)

        # return HttpResponse('{}注册成功!'.format(username))
        return response

    elif request.method == 'GET': # 获取注册页面
        return render(request, 'register.html')


# 登录
def login(request):
    if request.method == 'POST': # 登录操作
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 根据用户名和密码 去数据库中找
        # 能找到，登录成功
        # 找不到，登录失败
        users = User.objects.filter(u_name=username,u_password=password)
        if users.exists():  # 存在
            user = users.first()

            # 登录成功，直接重定向 首页
            response = redirect('/meituan/')

            # 设置cookie
            response.set_cookie('username', user.u_name)

            # return HttpResponse('{}登录成功'.format(user.u_name))
            return response

        else:   # 不存在
            return HttpResponse('用户名或密码错误!')

    elif request.method == 'GET': # 获取登录页面
        return render(request, 'login.html')

# 退出登录
def logout(request):
    # 删除cookie
    response = redirect('/meituan/')
    response.delete_cookie('username')

    return response


def about(request):
    # 获取cookie
    username = request.COOKIES.get('username')

    return render(request, 'about.html', context={'username':username})