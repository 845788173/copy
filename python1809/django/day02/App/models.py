from django.db import models



class Dog(models.Model):
    d_name = models.CharField(max_length=30)
    d_color = models.CharField(max_length=10)
    d_age = models.IntegerField()
    isdelete = models.BooleanField(default=False)

    class Meta():
        # 表名
        db_table = 'dog'
        # 修改默认排序 字段
        # ordering = ['id']
        ordering = ['d_age']

class Class1(models.Model):
    p_name=models.CharField(max_length=40)


class Student(models.Model):
    s_name=models.CharField(max_length=40)
    s_age=models.CharField(max_length=30)
    s_class1=models.ForeignKey(Class1)



