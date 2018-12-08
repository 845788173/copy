from django.conf.urls import url


from .views import *

urlpatterns=[
    #首页
    url(r'^home/',home,name='home'),
    # 闪购
    url(r'^market/$', market, name='market'),
    url(r'^marketwithparams/(\d+)/(\d+)/(\d+)/$', market_width_params, name='market_with_params'),

]