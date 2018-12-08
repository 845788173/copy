from django.db import models

class Lunbo(models.Model):
    id=models.IntegerField(primary_key=True)
    img=models.CharField(max_length=255)

class Goods(models.Model):
    id = models.IntegerField(primary_key=True)
    g_img=models.CharField(max_length=255)
    g_price=models.CharField(max_length=60)
    g_concent=models.CharField(max_length=255)

class User(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    token=models.CharField(max_length=255,default='')

class Cart(models.Model):
    user = models.ForeignKey(User)
    # 商品
    goods = models.ForeignKey(Goods)
    # 商品数量(选择)
    number = models.IntegerField()
    # 是否选中
    isselect = models.BooleanField(default=False)

class Order(models.Model):
    # 用户
    user = models.ForeignKey(User)
    # 创建时间
    createtime = models.DateTimeField(auto_now_add=True)
    # 状态
    # -1 过期
    # 1 未付款
    # 2 已付款，未发货
    # 3 已发货，快递
    # 4 已签收，未评价
    # 5 已评价
    # 6 退款....
    status = models.IntegerField(default=1)
    # 订单号
    identifier = models.CharField(max_length=256)


# 订单商品
# 一个订单 对应 多个商品
# 在从表中声明关系
class OrderGoods(models.Model):
    # 订单
    order = models.ForeignKey(Order)
    # 商品
    goods = models.ForeignKey(Goods)
    # 个数
    number = models.IntegerField(default=1)

    # 大小