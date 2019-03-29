from django.shortcuts import render,redirect
from django.http import HttpResponse
from HelloWord.models import User

# Create your views here.
def hello(request):
    return HttpResponse("hello word")

def index(request):
    return render(request,'index.html')
def login(request):
    # print("login登录测试获取表单")
    # print (request)
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #list = User.objects.all()
        #如果用户不存则返回登录页面
        try:
            #查询数据库
            user = User.objects.get(name=username)
        except:
            return render(request, 'login.html', {'msg': '用户名或者密码错误'})

        if password == user.password:
            return render(request, 'index.html')
        else:
            print("用户名称或者密码错误")
            return render(request, 'login.html',{'msg':'用户名或者密码错误'})

        #print(User.objects.filter('admin'))
        # if username == "leo" and password == "123456":
        #     return render(request,'index.html')
        # else:
        #     return HttpResponse("用户名或者密码错误")
        #测试打登录用户名称
        #print(request.POST.get('username'))

    return render(request,'login.html')