from django.shortcuts import render,redirect
from django.http import HttpResponse,StreamingHttpResponse
import os
import uuid
from app02.models import Dept

# Create your views here.
def gotoIndex(request):
    return render(request,"index.html")

def getData(request):
    var = request.GET.get('params',0)
    result='接收到客户端get参数消息请求数据：{0}'.format(var)
    return HttpResponse(result)

def add(request):
    num1=int(request.GET.get('num1',0))
    num2=int(request.GET.get('num2',0))
    num=num1+num2
    return HttpResponse('相加结果为：{0}'.format(num))

def getrestFul(request,bookname,year):
    result = '书名：{0}，出版年份：{1}'.format(bookname,year)
    return HttpResponse(result)

def hello(request):
    #处理post请求，接收表单提交的数据
    if request.POST :
        name = request.POST.get("inputname",None)
        result = 'hello,{0}'.format(name) if name.lower()!='monster' else 'go out!'
        return HttpResponse(result)
    else:
        #处理get请求，跳转页面
        return render(request,"hello.html")

def search(request):
    #处理post请求，接收表单提交的数据
    if request.POST :
        keyword = request.POST.get("keyword",None)
        #将要传递的数据放在字典中
        data = dict()
        data["keyword"]=keyword
        return render(request,"search.html")
    else:
        #处理get请求，跳转页面
        #return render(request,"hello")
        return redirect('/app02/gotosearch/')

def gotosearch(request):
    return render(request,'search.html')

def addCookie(request,company):
    #创建相应对象
    response =redirect('/app02/index/')
    #保存Cookie
    response.set_cookie('company',company)   
    #响应客户端
    return response

def getCookie(request):
    #从cookie中获取数据
    val = request.COOKIES.get('company',"")
    #跳转为首页，并显示cookie的值
    return render(request,'index.html',{'company':val})

def fileupload(request):
    if request.POST:
        #获取上传的文件对象
        obj = request.FILES.get('upfile',None)
        #创建上传文件的文件夹
        uploadDirPath = os.path.join(os.getcwd(),'app02/static/upfile')
        if not os.path.exists(uploadDirPath):
            os.mkdir(uploadDirPath)
        #拼接要上传的文件在服务器上的全路径
        fileFullPath = uploadDirPath + os.sep + obj.name
        #上传文件
        with open(fileFullPath,'wb+') as fp:
            for chunk in obj.chunks():
                fp.write(chunk)
        return render(request,'upload.html',{'msg':"文件上传成功"})
    else:
        return render(request,'upload.html')

def multifileupload(request):
    if request.POST:
        objs = request.FILES.getlist('upfile',None)
        uploadDirPath = os.path.join(os.getcwd(),'app02/static/upfile')
        if not os.path.exists(uploadDirPath):
            os.mkdir(uploadDirPath)
        for obj in objs:
            #拼接要上传的文件在服务器上的全路径
            fileFullPath = uploadDirPath + os.sep + obj.name
            #上传文件
            with open(fileFullPath,'wb+') as fp:
                for chunk in obj.chunks():
                    fp.write(chunk)
        return render(request,'upload.html',{'msg':"文件上传成功"})
    else:
        return render(request,'upload.html')

def pictureload(request):
    if request.POST:
        obj = request.FILES.get('upfile',None)
        #可接受的类型集合
        allowedType = ['.jpg','.png','.jpeg','.bmp']
        #获取扩展名
        fileType = os.path.splitext(obj.name)[1]
        if fileType in allowedType:
            uploadDirPath = os.path.join(os.getcwd(),'app02/static/upfile')
            if not os.path.exists(uploadDirPath):
                os.mkdir(uploadDirPath)
            #生成唯一文件名
            newName= str(uuid.uuid1())+fileType
            #拼接要上传的文件在服务器上的全路径
            fileFullPath = uploadDirPath+os.sep+newName
            #上传文件
            with open(fileFullPath,'wb+') as fp:
                for chunk in obj.chunks():
                    fp.write(chunk)
            #将文件在服务器上的地址回传以显示图片
            context = dict()
            context['url'] = 'upfile/' + newName
            context['msg'] = '文件上传成功'
            return render(request,'pictureload.html',context)
        else:
            return render(request,'pictureload.html',{'msg':"文件类型错误"})
    else:
        return render(request,'pictureload.html')

def filedownload(request,fileName):
    # 定义一个内部函数分块读取下文件数据
    def fileIterator(downloadFilePath, chunkSize=512):
        # 读取二进制文件
        with open(downloadFilePath, 'rb') as fp:
            while True:
                content = fp.read(chunkSize)
                if content:
                    yield content
                else:
                    break
    # 获取下载文件的全路径
    #obj = request.FILES.get('upfile',None)
    #fileName = os.path.splitext(obj.name)[0]
    downloadFilePath = os.getcwd() + '/app02/static/upfile/' + fileName
    print('下载文件的全路径：{0}'.format(downloadFilePath))
    # 响应客户端
    rep = StreamingHttpResponse(fileIterator(downloadFilePath))
    # 设置响应对象的关键值选项
    rep['Content-Type'] = 'application/octet-stream'
    rep['Content-Disposition'] = 'attachment;filename="{0}"'.format(fileName)
    return rep

#def valName(request,inputName):
    #模拟数据库查询，将查询结果放入列表


def deptAdd(request):
    if request.POST:
        #接收页面提交的数据
        dname = request.POST.get('danme',None)
        loc = request.POST.get('loc',None)
        #创建模型对象
        #dept = Dept(dname=dname,loc=loc)
        #调用save方法，向数据库添加一条数据
        #dept.save()
        
        return render(request,'deptAdd.html',{'msg':'添加成功'})
    else:
        return render(request,'deptAdd.html')


