from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^$', views.index, name='index'),    # 首页

    url(r'^randomview/$', views.randomview, name='randomview'),    # 项目抽取

    url(r'^goods/$', views.goods),
    url(r'^goods/(\d+)/$', views.goods, name='goods'),

    url(r'^detail/(\d+)/(\d+)/(\d+)/$', views.detail, name='detail'),

    url(r'^requesttest/$', views.requesttest),
    url(r'^gettest/$', views.gettest),
    url(r'^posttet/$', views.posttet),

    url(r'^responsetest/$', views.responsetest),




    #####
    url(r'^register/$', views.register),    # 注册
    url(r'^logout/$', views.logout),    # 退出
    url(r'^login/$', views.login),  # 登录
    url(r'^cart/$', views.cart),    # 购物车
]