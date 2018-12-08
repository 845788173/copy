from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^$', views.index),    # 首页

    url(r'^adddog/$', views.adddog),    # 添加狗
    url(r'^showdog/$', views.showdog),    # 显示狗


    #####  一对一
    url(r'^addperson/$', views.addperson),  # 添加一个人
    url(r'^addcard/$', views.addcard),  # 添加卡
    url(r'^delperson/$', views.delperson),  # 杀死某人
    url(r'^getpersoncard/$', views.getpersoncard),  # 获取人对应的身份证
    url(r'^getcardperson/$', views.getcardperson),  # 获取身份证对应人的信息


    #### 一对多
    url(r'^addgrade/$', views.addgrade), # 添加班级
    url(r'^addstudent/$', views.addstudent), # 添加学生
    url(r'^delgrade/$', views.delgrade), # 删除班级
    url(r'^showgrade/$', views.showgrade), # 获取班级对应人数
    url(r'^showstudent/$', views.showstudent), # 获取 学生 对应 班级

    #### 多对多
    url(r'^adduser/$', views.adduser),  # 添加用户
    url(r'^addgoods/$', views.addgoods),   # 添加商品
    url(r'^addcart/$', views.addcart),  # 添加到购物车
    url(r'^showcart/$', views.showcart),    # 显示购物车
    url(r'^addcollect/$', views.addcollect),    # 添加收藏
    url(r'^showgoods/$', views.showgoods),  # 显示商品(显示收藏数量)
]


