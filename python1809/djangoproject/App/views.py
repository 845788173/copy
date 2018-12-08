import hashlib
import random
import time
import uuid

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *

def zhuye(request):
    imgs=Lunbo.objects.all()
    imgs1=Goods.objects.all()
    token=request.session.get('token')
    user=User.objects.get(token=token)
    username=user.username
    return render(request,'html/zhuye.html',context={'imgs':imgs,'imgs1':imgs1,'username':username})

def spxq_param(request,img1id):
    good=Goods.objects.get(id=img1id)
    return render(request,'html/spxq.html',context={'good':good})

def generate_password(param):
    sha=hashlib.sha256()
    sha.update(param.encode())
    return sha.hexdigest()


def Register(request):
    if request.method=='GET':

        return render(request,'html/zhuce.html')
    elif request.method=="POST":
        user=User()
        user.username=request.POST.get('username')
        user.password=generate_password(request.POST.get('password'))
        user.token=str(uuid.uuid5(uuid.uuid4(),'register'))
        user.save()
        request.session['token']=user.token
        return redirect(reverse('liqun:zhuye'))

def Login(request):
    if request.method=='GET':
        return render(request,'html/denglu.html')
    elif request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
            if user.password==generate_password(password):

                user.token=str(uuid.uuid5(uuid.uuid4(),'login'))
                user.save()
                request.session['token']=user.token
                return redirect('liqun:zhuye')
            else:
                return render(request,'html/denglu.html')
        except:
            return render(request,'html/denglu.html')
def cart(request):
    token=request.session.get('token')
    if token:
        user=User.objects.get(token=token)
        carts=Cart.objects.filter(user=user).exclude(number=0)
        return render(request,'html/gouwuche.html',{'carts':carts})
    else:
        return redirect('liqun:login')

def addcart(request):
    goodid=request.GET.get('goodid')
    token=request.session.get('token')
    responseData={
        'status':1,
        'msg':'添加购物车成功',
    }

    if token:

        user=User.objects.get(token=token)
        print(user)
        goods=Goods.objects.get(pk=goodid)
        print(11111111)
        carts=Cart.objects.filter(user=user).filter(goods=goods)
        if carts.exists():
            cart=carts.first()
            cart.number+=1
            cart.save()
            responseData['number'] = cart.number
        else:
            print('1111111111')
            cart=Cart()
            cart.user=user
            cart.goods=goods
            cart.number=1
            cart.save()
            responseData['number'] = cart.number
        return JsonResponse(responseData)
    else:
        responseData['msg']='未登录，请登录'
        responseData['status']=-1
        return JsonResponse(responseData)
def subcart(request):
    token=request.session.get('token')
    goodid=request.GET.get('goodid')
    user=User.objects.get(token=token)
    goods=Goods.objects.get(pk=goodid)
    carts=Cart.objects.filter(user=user,goods=goods)
    cart = carts.first()
    print('###############')
    print(cart)
    if cart.number >0:
        cart.number-=1
    else:
        cart.number=0
    cart.save()
    responseData={
        'msg':'购物车删减数量成功',
        'status':1,
        'number':cart.number,
    }
    return JsonResponse(responseData)

def changecartstatus(request):
    cartid=request.GET.get('cartid')
    cart=Cart.objects.get(id=cartid)
    cart.isselect=not cart.isselect
    cart.save()
    responseData={
        'msg': '选中状态改变',
        'status': 1,
        'isselect': cart.isselect
    }
    return JsonResponse(responseData)

def changecartselect(request):
    isselect=request.GET.get('isselect')
    if isselect=='true':
        isselect=True
    else:
        isselect=False
    token = request.session.get('token')
    user = User.objects.get(token=token)
    carts = Cart.objects.filter(user=user)
    for cart in carts:
        cart.isselect = isselect
        cart.save()

    return JsonResponse({'msg': '反选操作成功', 'status': 1})

def generateorder(request):
    token = request.session.get('token')
    user = User.objects.get(token=token)
    # 生成订单
    order = Order()
    order.user = user
    order.identifier = str(int(time.time())) + str(random.randrange(10000,100000))
    order.save()

    # 订单商品
    carts = Cart.objects.filter(user=user).filter(isselect=True)
    for cart in carts:
        orderGoods = OrderGoods()
        orderGoods.order = order
        orderGoods.goods = cart.goods
        orderGoods.number = cart.number
        orderGoods.save()

        # 从购物车移除
        cart.delete()

    responseData = {
        'msg':'订单生成成功',
        'status': 1,
        'identifier': order.identifier
    }

    return JsonResponse(responseData)


def orderinfo(request, identifier):
    # 一个订单 对应 多个商品
    order = Order.objects.get(identifier=identifier)

    return render(request, 'html/orderinfo.html', context={'order':order})


def notifyurl(request):
    print(' xxx  订单支付成功，请发货')
    print(request.GET.get('subject'))
    return JsonResponse({'msg':'success'})


def returnurl(request):
    print('xxx 订单支付成功，进行页面跳转')
    return HttpResponse('进行页面跳转，回到axf.....')


def pay(request):
    # identifier = request.GET.get('identifier')

    # 支付url
    # url = alipay_axf.direct_pay(
    #     subject='测试订单 --- iphone X',    # 订单名称
    #     out_trade_no=identifier,    # 订单号
    #     total_amount=9.9,   # 付款金额
    #     return_url='http://112.74.55.3/axf/returnurl/'
    # )

    # 拼接支付网关
    # alipay_url = 'https://openapi.alipaydev.com/gateway.do?{data}'.format(data=url)

    # return JsonResponse({'alipay_url':alipay_url})
    pass
