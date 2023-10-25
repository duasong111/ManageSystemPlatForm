from django.shortcuts import render,redirect,HttpResponse
def user_list(request):
    data="123"

    return render(request,'user_list.html',{'data':data})