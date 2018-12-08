from django.conf.urls import url

from .views import *

urlpatterns=[
    url(r'^$',index),
    url(r'^adddog/$',adddog),

    #### 一对多
    url(r'^addgrade/$', addgrade),  # 添加班级
    url(r'^addstudent/$', addstudent),  # 添加学生
    url(r'^delgrade/$', delgrade),  # 删除班级
    url(r'^showgrade/$', showgrade),  # 获取班级对应人数
    url(r'^showstudent/$', showstudent),  # 获取 学生 对应 班级
]