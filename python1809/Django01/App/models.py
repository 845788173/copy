from django.db import models

# Create your models here.

# objects 系统生成的管理器 Manager类
# 自定义管理器 Manager类
class DogManager(models.Manager):
    def all(self):
        # 调用父类方法获取所有数据，然后在父类的基础上进行过滤
        return super().all().filter(isdelete=False)

# 狗模型类
class Dog(models.Model):
    d_name = models.CharField(max_length=30)
    d_color = models.CharField(max_length=10)
    d_age = models.IntegerField()
    isdelete = models.BooleanField(default=False)

    # 系统生成 objects
    myobjects = DogManager()

    # 类方法，方便实例化对象
    @classmethod
    def createDog(cls,name,color,age,isdelte=False):
        dog = cls(d_name=name,d_age=age, d_color=color, isdelete=isdelte)
        return dog

    def __str__(self):
        return self.d_name

    # 元选项
    class Meta():
        # 表名
        db_table = 'dog'
        # 修改默认排序 字段
        # ordering = ['id']
        ordering = ['d_age']



##### 一对一
# 人 模型类  【主表】
class Person(models.Model):
    p_name = models.CharField(max_length=80)
    p_age = models.IntegerField()


# 身份证 模型类 【从表】
class IDCard(models.Model):
    i_num = models.CharField(max_length=40)
    i_addr = models.CharField(max_length=256)

    # 声明关系
    ## 情况一: 默认models.CASECADE删除级联数据
    # 删除人时，身份证存在，人和身份证一起删除

    ## 情况二: models.PROTECT保护模式
    # 删除人时，身份证存在，抛出'ProtectedError'

    ## 情况三: models.SET_NULL 置空模式
    # 删除人时，身份证存在，设置为NULL
    i_person = models.OneToOneField(Person, on_delete=models.SET_NULL, null=True)

    ## 情况四: SET_DEFAULT 设置默认值
    # 删除人时，身份证存在，设置为默认值
    # i_person = models.OneToOneField(Person, on_delete=models.SET_DEFAULT, null=True, default=1)


##### 一对多
# 一个班级 对应 多个学生
# 班级模型类
class Grade(models.Model):
    g_name = models.CharField(max_length=100)

# 学生模型类
class Student(models.Model):
    s_name = models.CharField(max_length=40)
    s_score = models.IntegerField()

    # 声明关系
    s_grade = models.ForeignKey(Grade, on_delete=models.SET_DEFAULT, default=1)



##### 多对多
# 一个用户 对应添加 多个商品
# 一个商品 对应 多个用户收藏

# 用户模型类
class User(models.Model):
    u_name = models.CharField(max_length=100)
    u_tel =models.CharField(max_length=20)

# 商品模型类
class Goods(models.Model):
    g_name = models.CharField(max_length=100)
    g_price = models.IntegerField()

    # 声明关系
    g_user = models.ManyToManyField(User)

