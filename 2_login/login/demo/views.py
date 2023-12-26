from django.shortcuts import render, redirect

# Create your views here.

def login(request):
    # 判断到底是POST还是GET
    if request.method == "GET":
        # GET请求返回
        return render(request, 'login.html')
    else:
        # POST：用户提交的数据以post方式返回
        # 去请求体中获取数据再进行校验
        username = request.POST.get('user')
        passwoard = request.POST.get('pwd')

        # 获得后就可以去数据库中校验用户名+密码的合法性
        # 校验成功后跳转至后台管理界面 http://127.0.0.1:8000/index/ /index/
        if username == "root" and passwoard == "123":
            return redirect('/index/')
        
        # 不成功，再次让用户看到login.html页面，并提示用户名或密码错误
        return render(request, 'login.html', {"error": "用户名或密码错误"}) 
    

def index(request):
    return render(request, 'index.html')
