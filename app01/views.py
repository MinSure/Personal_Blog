from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
Username = []
Userpwd = []

def gotoIndex(request):
    '跳转至app01应用的index.html页面'
    return render(request,'index.html')

def gotoReg(request):
    return render(request, 'register.html')

def login(request):
    if request.POST :
        name = request.POST.get('username',None)
        pwd = request.POST.get("pwd",None)
        remember = request.POST.getlist("rem",None)
        val = request.session.get('user',None)
        num=val.index(name)
        if name ==Username[num] and pwd== Userpwd[num] :
        #if request.session[name]== pwd:
            #将账号密码加密存入cookie
            response = redirect('/app01/home')
            if remember:
                response.set_signed_cookie('account',name,salt='aaa')
                response.set_signed_cookie("password",pwd,'aaa')
            else:
                response.set_signed_cookie('account',name,salt='aaa')
                response.set_signed_cookie("password","",salt='aaa')
            #将账号信息存放到session中
            request.session['account'] = name
            request.session['password'] = pwd
            return response
        else:
            return render(request,'login.html',{'msg':"账号或密码错误"})
    else:
        account = request.get_signed_cookie('account',"",salt="aaa")
        password = request.get_signed_cookie('password',"",salt="aaa")
        return render(request,'login.html',{'account':account,'password':password})


def home(request):
    if request.POST :
        user = request.POST.get('user',None)
        pwd = request.POST.get("pwd",None)
        if user in Username:
            return render(request,'register.html',{'msg':"昵称已占用，请换一个！"})
        else:
            Username.append(user)
            Userpwd.append(pwd)
            request.session['user'] = Username
            request.session['pwd'] = Userpwd
            return render(request,'login.html',{'msg':"注册成功！"})
    else:
        #从session中获得账号，如果能获取则跳转到home页面，否则转会登陆页面
        account = request.session.get('account',None)
        if account:
            return render(request,'home.html',{'account':account})
        else:
            return render(request,'login.html',{'msg':"请先登录"})


def logout(request):
    #删除session中的account
    del request.session ['account']
    return redirect('/app01/login')