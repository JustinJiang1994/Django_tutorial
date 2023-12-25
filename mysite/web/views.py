from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse,render, redirect

def login(request):
    # return HttpResponse("登录页")  # 返回文本
    # return redirect("http://baidu.com")  # 跳转
    return render(request, "login.html")  # 返回login.html这个页面

