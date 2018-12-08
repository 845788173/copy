from django.conf.urls import url

from meituan import views

urlpatterns = [
    url(r'^$', views.index, name='index'),  # 首页

    url(r'^verifycode/$', views.verifycode, name='verifycode'), # 生成验证码

    # 路径参数
    url(r'^args01/(\d+)/$', views.args01, name='args01'),  # 带一个参数
    # 路径参数
    url(r'^args02/(\d+)/(\d+)/$', views.args02, name='args02'),

    # 测试
    url(r'^test01/$', views.test01, name='test01'),


    # request 对象
    url(r'testrequest', views.testrequest, name='testrequest'),
    # get 请求
    url(r'testget', views.testget, name='testget'),
    # post 请求
    url(r'testpost', views.testpost, name='testpost'),

    # response 对象
    url(r'testresponse', views.testresponse, name='testresponse'),
    url(r'testjson', views.testjson, name='testjson'),




    ## 会话技术cookie
    # 注册
    url(r'^register/$', views.register, name='register'),

    # 登录
    url(r'^login/$', views.login, name='login'),

    # 退出登录
    url(r'^logout/$', views.logout, name='logout'),

    # 关于
    url(r'^about/$', views.about, name='about'),
]