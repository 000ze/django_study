"""untitled2 URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
                             # 保存了路径和函数的对应关系
from django.conf.urls import url
from django.contrib import admin

from django.shortcuts import HttpResponse
from django.shortcuts import render
#request参数保存了所有和用户浏览器请求相关的数据
def h1(request):
    return HttpResponse('hello world')
def h2(request):
    return HttpResponse('hello people')
def h3(request):
    return HttpResponse('hello')

urlpatterns = [
    url(r'^1234/', h1),
    url(r'^5678/', h2),
    url(r'^', h3),
]
