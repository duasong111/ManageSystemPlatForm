from django.shortcuts import render,redirect,HttpResponse
from adminManage import models

from user.views.user import user_list


def admin_list(request):
    """管理员"""
    quaryset = models.Admin.objects.all()
    contest={
         "quaryset":quaryset
    }
    # m=user_list(request)
    # print(m)
    # return HttpResponse(contest)
    return render(request,'admin_list.html',contest)