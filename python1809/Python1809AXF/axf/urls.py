from django.conf.urls import url

from axf import views

urlpatterns = [
    url(r'^$', views.home, name='index'),  # 首页
    url(r'^home/$', views.home, name='home'),   # 首页
    url(r'^market/(\d+)/(\d+)/(\d+)/$', views.market, name='market'), # 闪购超市
    url(r'^cart/$', views.cart, name='cart'),   # 购物车
    url(r'^mine/$', views.mine, name='mine'),   # 我的


    url(r'^registe/$', views.registe, name='registe'),  # 注册
    url(r'^checkaccount/$', views.checkaccount, name='checkaccount'), # 账号验证
    url(r'^logout/$', views.logout, name='logout'), # 退出
    url(r'^login/$', views.login, name='login'),    # 登录

    url(r'^addcart/$', views.addcart, name='addcart'),  # 添加购物车
    url(r'^subcart/$', views.subcart, name='subcart'),  # 购物车减操作
    url(r'^changecartstatus/$', views.changecartstatus, name='changecartstatus'), # 修改选中状态
    url(r'changecartselect/$', views.changecartselect,name='changecartselect'), # 全选/取消全选

    url(r'^generateorder/$', views.generateorder, name='generateorder'),    # 下单
    url(r'^orderinfo/(\d+)/$', views.orderinfo, name='orderinfo'),

    url(r'^pay/$', views.pay, name='pay'),  # 支付
    url(r'^notifyurl/$', views.notifyurl, name='notifyurl'), # 支付完成后的通知
    url(r'^returnurl/$', views.returnurl, name='returnurl'),    # 支付完成后的跳转
]