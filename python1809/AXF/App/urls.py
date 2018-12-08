from django.conf.urls import url
from .views import *

urlpatterns = [
    # 首页
    url(r'^home/$', home, name='home'),

    # 闪购
    url(r'^market/$', market, name='market'),
    url(r'^marketwithparams/(\d+)/(\d+)/(\d+)/$', market_width_params, name='market_with_params'),

    # 我的
    url(r'^mine/$', mine, name='mine'),
    url(r'^register/$', register, name='register'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),

    # 购物车
    url(r'^cart/$', cart, name='cart'),
    url(r'^cartadd/$', cart_add, name='cart_add'),
    url(r'^cartnumadd/$', cart_num_add, name='cart_num_add'),
    url(r'^cartnumreduce/$', cart_num_reduce, name='cart_num_reduce'),
    url(r'^cartdel/$', cart_del, name='cart_del'),
    url(r'^cartselect/$', cart_select, name='cart_select'),
    url(r'^cartselectall/$', cart_selectall, name='cart_selectall'),

]


