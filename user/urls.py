"""定义learning_logs的URL模式"""
from django.conf.urls import url
from user.views import user
from . import views
urlpatterns = [
    #其实这里的就是相当与他们的子数据，这样就可以不用去表现出那么多url的路径了，
#使用这个就是
    url(r'^list$', user.user_list, name='list'),
    # url(r'Get$',views.GetMyscore,name='GetMyscore'),
    # url(r'^test', views.TestView,name="test")
]