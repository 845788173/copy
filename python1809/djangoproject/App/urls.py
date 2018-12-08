from django.conf.urls import url

from .views import *




urlpatterns=[
    url(r'^zhuye/$',zhuye,name='zhuye'),
    # url(r'^spxq/(\d+)/$',spxq,name='spxq'),
    url(r'^spxqparam/(\d+)/$',spxq_param,name='spxq_param'),
    url(r'^register/$',Register,name='regiser'),
    url(r'^login/$',Login,name='login'),
    url(r'^cart/$',cart,name='cart'),
    url(r'^cartadd/$',addcart,name='cartadd'),
    url(r'^subcart/$',subcart,name='subcart'),
    url(r'^changecartstatus/$',changecartstatus,name='changecartstatus'),
    url(r'^changecartselect/$',changecartselect,name='changecartselect'),
    url(r'^generateorder/$', generateorder, name='generateorder'),  # 下单
    url(r'^orderinfo/(\d+)/$', orderinfo, name='orderinfo'),
    url(r'^pay/$', pay, name='pay'),  # 支付
    url(r'^notifyurl/$', notifyurl, name='notifyurl'), # 支付完成后的通知
    url(r'^returnurl/$', returnurl, name='returnurl'),
]