from django.db import models

class Main(models.Model):
    img=models.CharField(max_length=200)
    name=models.CharField(max_length=30)
    trackid=models.CharField(max_length=20)
    class Meta:
        abstract=True


class MainWheel(Main):
    class Meta:
        db_table='axf_wheel'

class MainNav(Main):
    class Meta:
        db_table='axf_nav'

class MainMustbuy(Main):
    class Meta:
        db_table='axf_mustbuy'

class MainShop(Main):
    class Meta:
        db_table='axf_shop'



# 显示的商品数据
class MainShow(Main):
    categoryid = models.CharField(max_length=30)
    brandname = models.CharField(max_length=30)

    img1 = models.CharField(max_length=200)
    childcid1 = models.CharField(max_length=30)
    productid1 = models.CharField(max_length=30)
    longname1 = models.CharField(max_length=100)
    price1 = models.CharField(max_length=30)
    marketprice1 = models.CharField(max_length=30)

    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=30)
    productid2 = models.CharField(max_length=30)
    longname2 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=30)
    marketprice2 = models.CharField(max_length=30)

    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=30)
    productid3 = models.CharField(max_length=30)
    longname3 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=30)
    marketprice3 = models.CharField(max_length=30)

    class Meta:
        db_table = 'axf_mainshow'


# 商品分类
class FoodType(models.Model):
    typeid = models.CharField(max_length=20)
    typename = models.CharField(max_length=20)
    childtypenames = models.CharField(max_length=200)
    typesort = models.IntegerField()

    class Meta:
        db_table = 'axf_foodtypes'
# 商品数据
class Goods(models.Model):
    productid = models.CharField(max_length=20)
    productimg = models.CharField(max_length=200)
    productname = models.CharField(max_length=50)
    productlongname = models.CharField(max_length=50)
    isxf = models.BooleanField(default=False)

    pmdesc = models.IntegerField()
    specifics = models.CharField(max_length=20)
    price = models.FloatField()
    marketprice = models.FloatField()
    categoryid = models.CharField(max_length=20)

    childcid = models.CharField(max_length=20)
    childcidname = models.CharField(max_length=30)
    dealerid = models.CharField(max_length=20)
    storenums = models.IntegerField()
    productnum = models.IntegerField()

    class Meta:
        db_table = 'axf_goods'

# 商品数据
class Goods(models.Model):
    productid = models.CharField(max_length=20)
    productimg = models.CharField(max_length=200)
    productname = models.CharField(max_length=50)
    productlongname = models.CharField(max_length=50)
    isxf = models.BooleanField(default=False)

    pmdesc = models.IntegerField()
    specifics = models.CharField(max_length=20)
    price = models.FloatField()
    marketprice = models.FloatField()
    categoryid = models.CharField(max_length=20)

    childcid = models.CharField(max_length=20)
    childcidname = models.CharField(max_length=30)
    dealerid = models.CharField(max_length=20)
    storenums = models.IntegerField()
    productnum = models.IntegerField()

    class Meta:
        db_table = 'axf_goods'


# 用户
class User(models.Model):
    name = models.CharField(max_length=18, unique=True)
    pwd = models.CharField(max_length=32)
    email = models.CharField(max_length=30, null=True,blank=True)
    icon = models.CharField(max_length=50, default='')
    gender = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)


# 购物车
class Cart(models.Model):
    goods = models.ForeignKey(Goods)
    user = models.ForeignKey(User)
    num = models.IntegerField(default=1)
    is_select = models.BooleanField(default=True)

