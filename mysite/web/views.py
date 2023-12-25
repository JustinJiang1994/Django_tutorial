from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse, render, redirect


def login(request):
    # return HttpResponse("登录页")  # 返回文本
    # return redirect("http://baidu.com")  # 跳转
    return render(request, "login.html")  # 返回login.html这个页面


def user_list(request):
    # 1. 数据库中获取所有的用户列表
    data = ["user1", "user2", "user3"]
    mapping_dict = {"name":"user1", "age":18, "size":10}

    # 2. 打开文件并读取内容

    # 3. 模版的渲染 -> 文本替换

    # 新增回传的参数，以字典形式表示
    return render(request, "user_list.html", {"message": "标题来了", "data_list": data, "mapping_dict":mapping_dict})
