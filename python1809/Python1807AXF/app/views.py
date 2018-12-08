from django.shortcuts import render
from app.models import Wheel



# 首页
def home(request):
    # 轮播图数据
    wheels = Wheel.objects.all()

    data = {
        'title': '首页',
        'wheels':wheels
    }

    return render(request, 'home.html', context=data)

# 闪购超市
def market(request):
    return render(request, 'market.html')

# 购物车
def cart(request):
    return render(request, 'cart.html')

# 我的
def mine(request):
    return render(request, 'mine.html')