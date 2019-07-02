from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def gotoIndex(request):
    '跳转至app01应用的index.html页面'
    return render(request,'index.html', context={
                      'title': '博客首页', 
                      'welcome': 'Blog在线登陆'
    })

def gotoReg(request):
    return render(request, 'register.html')