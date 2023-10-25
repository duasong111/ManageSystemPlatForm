
from django.contrib import admin
from django.urls import path
# from adminManage.views.admin import
from django.conf.urls import include, url
# from django.contrib import adminManage
urlpatterns = [
    # path('adminManage/', adminManage.site.urls), #这俩是系统自带的登录页面，目前我先不去使用
    # path('user/list/',adminManage.admin_list),
    #这种就是使用一个大路径，然后再将大的路径分为若干个小的路径
    path('adminManage/', include(('adminManage.urls', 'adminManage'), namespace='adminManage')),
    path('user/', include(('user.urls', 'user'), namespace='user')),
    # path('user/list/',adminManage.admin_list),
]
