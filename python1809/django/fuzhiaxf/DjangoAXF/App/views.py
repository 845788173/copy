from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse

from AXF.settings import MEDIA_ROOT
from .models import *
import uuid
import hashlib
import os


######################### 首页  #########################
# 首页
def home(request):

    # 获取首页数据
    # 轮播数据
    wheels = MainWheel.objects.all()
    # 导航数据
    navs = MainNav.objects.all()
    # 必购数据
    mustbuys = MainMustbuy.objects.all()
    # shop数据
    shops = MainShop.objects.all()
    shops0 = shops.first()
    shops1_2 = shops[1:3]
    shops3_6 = shops[3:7]
    shops7_10 = shops[7:11]
    # 显示的商品数据
    mainshows = MainShow.objects.all()

    data = {
        "wheels": wheels,
        "navs": navs,
        "mustbuys": mustbuys,
        "shops0": shops0,
        "shops1_2": shops1_2,
        "shops3_6": shops3_6,
        "shops7_10": shops7_10,
        "mainshows": mainshows,
    }

    # 渲染
    return render(request, 'home/home.html', context=data)


######################### 闪购  #########################
# 闪购
def market(request):
    return redirect(reverse('AXF:market_with_params', args=['104749', "0", "0"]))


def market_width_params(request, typeid, childid, sortid):
    # 获取主分类数据
    foodtypes = FoodType.objects.all()

    # 获取商品数据
    # goods_list = Goods.objects.all()[:10]  # 获取前10条商品数据
    goods_list = Goods.objects.filter(categoryid=typeid)  # 获取对于主分类的商品数据
    # 根据子分类id来继续筛选商品
    if childid != "0":  # 不是‘全部分类’
        goods_list = goods_list.filter(childcid=childid)

    # 获取当前主分类下的子分类数据
    child_foodtype = foodtypes.filter(typeid=typeid).first()
    child_foodtype_str = child_foodtype.childtypenames
        # “全部分类:0#酸奶乳酸菌:103537#牛奶豆浆:103538#面包蛋糕:103540”
    child_type_list = child_foodtype_str.split('#')
        # ['全部分类:0', '酸奶乳酸菌:103537', '牛奶豆浆:103538', '面包蛋糕:103540']
    childtypes = []
    for string in child_type_list:
        # string: '全部分类:0'
        list1 = string.split(":")
        childtypes.append({"childtypename": list1[0], "childtypeid": list1[1]})
    # print(childtypes)
        #[
        #   {'childtypename': '全部分类', 'childtypeid': '0'},
        #   {'childtypename': '酸奶乳酸菌', 'childtypeid': '103537'},
        #   {'childtypename': '牛奶豆浆', 'childtypeid': '103538'},
        #   {'childtypename': '面包蛋糕', 'childtypeid': '103540'}
        #]

    # 综合排序
    if sortid == '0':  # 综合排序
        pass
    # 销量排序
    elif sortid == '1':
        goods_list = goods_list.order_by('-productnum')
    # 价格降序
    elif sortid == '2':
        goods_list = goods_list.order_by('-price')
    # 价格升序
    elif sortid == '3':
        goods_list = goods_list.order_by('price')


    data = {
        "foodtypes": foodtypes,
        "goods_list": goods_list,
        "typeid": typeid,
        "childtypes": childtypes,
        "childid": childid,
    }

    return render(request, 'market/market.html', data)


######################### 我的  #########################
# 我的
def mine(request):
    data = {
        "name": "",
        "icon": "",
    }
    # 获取当前用户的信息
    userid = request.session.get('userid', 0)
    users = User.objects.filter(id=userid)
    if users.exists():
        data["name"] = users.first().name
        data["icon"] = users.first().icon
    return render(request, 'mine/mine.html', data)

# 注册
def register(request):
    if request.method == "POST":
        # 获取前端提交过来的参数
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        icon = request.FILES.get('file')

        # 后台验证
        if len(username) < 6:
            data = {
                'msg': "用户名长度至少为6位"
            }
            return render(request, 'user/register.html', data)

        # 先检测用户名是否存在
        users = User.objects.filter(name=username)
        if users.exists():
            data = {
                'msg': "用户名已存在！"
            }
            return render(request, 'user/register.html', data)

        # 注册
        user = User()
        user.name = username
        user.pwd = password
        user.email = email
        # print("icon:", icon)
        # 如果上传了头像
        if icon:
            # 将图片存入后台
            icon_name = generate_icon() + os.path.splitext(icon.name)[-1]
            icon_path = os.path.join(MEDIA_ROOT, icon_name)
            with open(icon_path, 'ab') as fp:
                for part in icon.chunks():
                    fp.write(part)
                    fp.flush()

            # 将图片路径存入数据库
            user.icon = "/upload/" + icon_name

        user.save()

        # 注册成功后,自动登录，跳转到首页（‘我的’页面）
        request.session['userid'] = user.id  # 自动登录（保存登录状态）
        return redirect(reverse('AXF:mine'))

    else:
        return render(request, 'user/register.html')


# 生成随机唯一的图片名
def generate_icon():
    uid = str(uuid.uuid4())
    return my_md5(uid)


# md5加密
def my_md5(string):
    m = hashlib.md5()
    m.update(string.encode())
    return m.hexdigest()


# 退出
def logout(request):
    del request.session['userid']
    request.session.flush()
    return redirect(reverse('AXF:mine'))


# 登录
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





######################### 购物车  #########################
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


# ######################### 订单  #########################
# 订单页面
def order(request, oid):
    order = Order.objects.get(id=oid)
    return render(request, 'order/order.html', {"order": order})


# 生成订单
def order_add(request):
    data = {
        "status": 1,
        "msg": "success",
    }
    userid = request.session.get('userid', 0)
    if not userid:
        data['status'] = 0
        data['msg'] = "请先登录！"
    else:
        if request.method == "POST":

            # 先检测购物车中是否有选中商品
            carts = Cart.objects.filter(user_id=userid, is_select=True)
            if not carts.exists():
                data['status'] = -3
                data['msg'] = "请选择商品后再结算！"

            else:
                # 生成订单
                #   1, 给订单表添加一条数据
                #   2, 给订单商品表添加当前订单的商品数据

                # 1, 给订单表添加一条数据
                order = Order()
                # 订单号： 由后台创建，唯一性
                order.order_id = my_md5(str(uuid.uuid4()))
                order.user_id = userid
                order.save()

                # 2, 给订单商品表添加当前订单的商品数据
                #  获取当前用户购物车中所有选中的商品
                carts = Cart.objects.filter(user_id=userid, is_select=True)
                total = 0  # 订单总价
                for cart in carts:
                    order_goods = OrderGoods()
                    order_goods.goods_id = cart.goods_id
                    order_goods.num = cart.num
                    order_goods.order_id = order.id
                    order_goods.save()
                    # 计算总价
                    total += order_goods.num * order_goods.goods.price

                order.order_price = total
                order.save()

                # 删除购物车中已经生成订单的商品
                carts.delete()

                # 同时返回当前的订单id给前端
                data['oid'] = order.id

        else:
            data['status'] = -1
            data['msg'] = "请求方式有误！"

    return JsonResponse(data)


# 订单状态修改
def order_status_change(request):
    data = {
        "status": 1,
        "msg": "success",
    }
    userid = request.session.get('userid', 0)
    if not userid:
        data['status'] = 0
        data['msg'] = "请先登录！"
    else:
        if request.method == "POST":
            oid = request.POST.get('oid')
            status = request.POST.get('status')

            # 修改订单状态
            Order.objects.filter(id=oid).update(order_status=status)

        else:
            data['status'] = -1
            data['msg'] = "请求方式有误！"

    return JsonResponse(data)


# 待付款订单
def order_unpay(request):
    # 获取所有待付款订单
    orders = Order.objects.filter(order_status=0)
    return render(request, 'order/order_unpay.html', {"orders": orders})


# 待收货订单
def order_paid(request):
    # 获取所有待收货订单
    orders = Order.objects.filter(order_status=1)
    return render(request, 'order/order_paid.html', {"orders": orders})






