import hashlib
import uuid

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *


def home(request):


    #获取轮播数据
    wheels=MainWheel.objects.all()
    #获取导航数据
    navs=MainNav.objects.all()
    #获取必购数据
    mustbuys=MainMustbuy.objects.all()
    #获取shop数据
    shops=MainShop.objects.all()
    shops0=shops.first()
    shops1_2=shops[1:3]
    shops3_6=shops[3:7]
    shops7_10=shops[7:11]
    #获取商品数据
    mainshows=MainShow.objects.all()

    data={
        'wheels':wheels,
        'navs':navs,
        'mustbuys':mustbuys,
        'shops':shops,
        'shops1_2':shops1_2,
        'shops3_6':shops3_6,
        'shops7_10':shops7_10,
        'mainshows':mainshows,
    }

    return render(request,'home/home.html',context=data)

#闪购
def market(request):
    return redirect(reverse('AXF:market_with_params', args=['104749', "0", "0"]))

def market_with_params(request,typeid,childid,sortid):
    #主分类数据
    foodtypes=FoodType.objects.all()
    #获取商品数据
    goods_list=Goods.objects.filter(categoryid=typeid)
    #不是主分类的的数据
    if childid !='0':
        goods_list=goods_list.objects.filter(childcid=childid)
        #获取主分类下的字分类数据
    child_foodtype=foodtypes.objects.filter(typeid=typeid)

    child_type_list=child_food_type_str.split('#')
    childtypes=[]
    for string in child_type_list:
        list1=string.split(':')
        childtypes.append({'childtypename':list1[0],'childtypeid':list[1]})



def mine(request):
    data={
        'name':'',
        'icon':''
    }
    #获取前端的数据
    userid=request.session.get('userid',0)
    users=User.objects.filter(id=userid)
    data['name']=users.first().name
    data['icon']=users.first().icon
    return render(request, 'mine.html', data)


    #注册
    if request.method=='POST':
        #获取前端提交过来的数据
        username=request.POST.get('username')
        password=request.POST.get('password')
        icon=request.FILES.get('icon')
        email=request.POST.get('email')

    #后台验证
        if len(username)<6:
            data={
                'msg':'你的用户名小于6位，请输入正确的用户名'
            }
            return render(request, 'register/register.html', data)

        #验证用户名是否存在
        users=User.objects.filter(name=username)
        if users.exists():
            data={
                'msg':'用户已经存在，请重新输入'
            }
            return render(request,'register/register.html',data)
        #注册
        user=User()
        user.name=username
        user.password=password
        user.email=email

        #如果图片存在
        if icon:
            icon_name=genarate_icon+os.path.splitext(icon.name)[1]
            icon_path=os.path.join(MEDIA_ROOT,icon_name)
            with open('icon_path','ab')as fp:
                for part in icon.chunks():
                    fp.write(part)
                    fp.flush()


        #将图片路径存到数据库里
        user_path='/upload/'+icon_name
        user.save()

        #注册成功后自动跳转到首页
        request.session['userid']=user.id
        return redirect(reverse('AXF:index'))
    else:
        return render(request,'user/register.html')

    #生成随机名字
    def generate_icon():
        uid=str(uuid.uuid4())
        return my_md5(uid)
    def my_md5(string):
        m=hashlib.md5()
        m.update(string.encode())
        return m.hexidigest()

    #退出
    def logout(request):
        del request.session['userid']
        request.session.flush()
        return redirect(reverse('AXF:mine'))
    #登入
    def login(request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            # 登录验证
            users = User.objects.filter(name=username, pwd=password)
            if users.exists():
                # 登录成功,保存登录状态，然后自动跳转到‘我的’页面
                request.session['userid'] = users.first().id
                return redirect(reverse('AXF:mine'))
            else:
                data = {
                    "msg": '用户名或密码不正确'
                }
                return render(request, 'user/login.html', data)

        else:
            return render(request, 'user/login.html')

# 购物车
def cart(request):

    # 先判断是否登录
    userid = request.session.get('userid', 0)
    if not userid:
        # 未登录，进入登录页面
        return redirect(reverse('AXF:login'))

    # 如果登录了，则获取当前用户的购物车商品数据
    carts = Cart.objects.filter(user_id=userid)
    return render(request, 'cart/cart.html', {"carts": carts})


# 加入购物车
def cart_add(request):

    data = {
        "status": 1,
        "msg": "success",
    }

    # 先判断是否有用户登录
    userid = request.session.get('userid', 0)
    if not userid:
        # 没有用户登录
        data['status'] = 0
        data['msg'] = '您还没有登录，请先登录！'

    else:
        # 用户已登录
        if request.method == "GET":
            goodsid = request.GET.get('goodsid')
            num = request.GET.get('num')

            # 判断当前购物车是否已经存在该商品
            # 1,如果存在则只增加数量
            # 2,如果不存在则添加到购物车中

            carts = Cart.objects.filter(goods_id=goodsid, user_id=userid)
            # 1,如果存在则只增加数量
            if carts.exists():
                cart = carts.first()
                cart.num = cart.num + int(num)
                cart.save()
            # 2,如果不存在则添加到购物车中
            else:
                try:
                    # 加入购物车
                    cart = Cart()
                    cart.user_id = userid
                    cart.goods_id = goodsid
                    cart.num = num
                    cart.save()
                except:
                    data['status'] = -2
                    data['msg'] = '加入购物车失败！'

        else:
            data['status'] = -1
            data['msg'] = '请求方式有误！'

    return JsonResponse(data)


# 购物车数量增加
def cart_num_add(request):
    data = {
        "status": 1,
        "msg": "success",
    }

    # 先判断是否登录
    userid = request.session.get('userid', 0)
    if not userid:
        data["status"] = 0
        data['msg'] = "用户未登录，请先登录！"

    else:
        if request.method == "POST":
            cartid = request.POST.get('cartid')

            carts = Cart.objects.filter(id=cartid)
            if carts.exists():
                cart = carts.first()
                cart.num = cart.num + 1
                cart.save()

                # 修改成功后，返回最新的商品数量
                data["num"] = cart.num
            else:
                data["status"] = -1
                data['msg'] = "当前商品不存在！"

        else:
            data["status"] = -2
            data['msg'] = "请求方式错误！"

    return JsonResponse(data)


# 购物车数量减少
def cart_num_reduce(request):
    data = {
        "status": 1,
        "msg": "success",
    }

    # 先判断是否登录
    userid = request.session.get('userid', 0)
    if not userid:
        data["status"] = 0
        data['msg'] = "用户未登录，请先登录！"

    else:
        if request.method == "POST":
            cartid = request.POST.get('cartid')

            carts = Cart.objects.filter(id=cartid)
            if carts.exists():
                cart = carts.first()
                if cart.num > 1:
                    cart.num = cart.num - 1
                cart.save()

                # 修改成功后，返回最新的商品数量
                data["num"] = cart.num
            else:
                data["status"] = -1
                data['msg'] = "当前商品不存在！"

        else:
            data["status"] = -2
            data['msg'] = "请求方式错误！"

    return JsonResponse(data)


# 删除
def cart_del(request):
    data = {
        "status": 1,
        "msg": "success",
    }

    userid = request.session.get('userid', 0)
    if not userid:
        data["status"] = 0
        data["msg"] = "尚未登录，请先登录!"
    else:
        if request.method == "POST":
            cartid = request.POST.get('cartid')
            # 删除
            Cart.objects.filter(id=cartid).delete()

        else:
            data["status"] = -1
            data["msg"] = "请求方式错误!"

    return JsonResponse(data)


# 勾选/取消勾选
def cart_select(request):
    data = {
        "status": 1,
        "msg": "success",
    }

    userid = request.session.get('userid', 0)
    if not userid:
        data["status"] = 0
        data["msg"] = "尚未登录，请先登录!"
    else:
        if request.method == "POST":
            cartid = request.POST.get('cartid')
            # 勾选/取消勾选
            carts = Cart.objects.filter(id=cartid)
            if carts.exists():
                cart = carts.first()
                cart.is_select = not cart.is_select
                cart.save()
                data['select'] = cart.is_select

        else:
            data["status"] = -1
            data["msg"] = "请求方式错误!"

    return JsonResponse(data)


# 全选 / 全不选
def cart_selectall(request):
    data = {
        "status": 1,
        "msg": "success",
    }

    userid = request.session.get('userid', 0)
    if not userid:
        data["status"] = 0
        data["msg"] = "尚未登录，请先登录!"
    else:
        if request.method == "POST":
            # 获取前端提交过来之前的‘全选’状态
            is_all_select = int(request.POST.get('isAllSelect'))

            # 如果当前是全选的则将当前用户购物车中所有商品的选中状态更改为不选中(is_select=False)
            # 如果当前是不全选的则将当前用户购物车中所有商品的选中状态更改为选中(is_select=True)
            Cart.objects.filter(user_id=userid).update(is_select=not is_all_select)
            # 将最新的‘全选’状态返回给前端
            data['selectall'] = not is_all_select

        else:
            data["status"] = -1
            data["msg"] = "请求方式错误!"

    return JsonResponse(data)

