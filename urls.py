"""day2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app02 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app02/index/',views.gotoIndex),
    path('app02/senddata/', views.getData),
    path('app02/add/', views.add),
    path('app02/bookinfo/<str:bookname>/<int:year>', views.getrestFul),
    path('app02/hello/', views.hello),
    path('app02/search/', views.search),
    path('app02/gotosearch/', views.gotosearch),
    path('app02/addCookie/<str:company>/', views.addCookie),
    path('app02/getCookie/', views.getCookie),
    path("app02/fileupload/",views.fileupload),
    path("app02/multifileupload",views.multifileupload),
    path('app02/pictureload/',views.pictureload),
    path('app02/filedownload/<str:fileName>',views.filedownload),
    path('app02/dept/add/',views.deptAdd)
]
