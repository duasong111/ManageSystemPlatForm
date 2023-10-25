from django.forms import models
from django.forms import ModelForm
from django.shortcuts import render,HttpResponse,redirect
from django import forms
# from user import models
from django.conf import settings
from user.utils.bootstrap import BootStrapForm
from user.utils.bootstrap import BootStrapModelForm
import os

class UpForm(BootStrapForm):
    bootstrap_exclude_fields = ['img']
    name = forms.CharField(label="姓名")
    email = forms.CharField(label="邮箱")
    img = forms.FileField(label="头像")

class UpModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ['img']
    class Meta:
        model =models.City
        fields="__all__"
def user_add(request):
    """使用modelForm来进行图片的保存，上传"""
    title = "ModelForm上传文件"
    if request.method == "GET":
        form = UpModelForm()
        return render(request, 'MainViews.html', {"form": form, 'title': title})

    form = UpModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponse("上传成功")
    return render(request, 'MainViews.html', {"form": form, 'title': title})