from django.shortcuts import render, redirect

# Create your views here.

from Models.models import *
from Models.From import *


def Home(request):
    u = Userinfo.objects.all()
    return render(request, 'index.html', {'userinfo': u, 'title': "首页"})


def GetUserinfo(request):
    u = Userinfo.objects.all()
    return render(request, 'showUserinfo.html', {'userinfo': u, 'title': "用户信息"})


def GetHostinfo(request):
    h = Hostinfo.objects.all()
    return render(request, 'showHostinfo.html', {'hostinfo': h, 'title': "主机信息"})


def GetLoginfo(request):
    l = Loginfo.objects.all()
    return render(request, 'showLoginfo.html', {'loginfo': l, 'title': "日志信息"})
