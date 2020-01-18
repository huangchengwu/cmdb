from django.shortcuts import render, redirect
from Models.models import *
from Models.From import *


def AddUserinfo(request):
    if request.method == 'GET':
        From = UserinfoForm()
        return render(request, 'addUserinfo.html', {'From': From, 'title': "添加用户信息"})
    else:
        sub_From = UserinfoForm(request.POST)
        if sub_From.is_valid():
            sub_From.save()
        return redirect(request, 'sub.html', {'sub_From': sub_From})


def AddHostinfo(request):
    if request.method == 'GET':
        From = HostinfoForm()
        return render(request, 'addHostinfo.html', {'From': From, 'title': "添加主机信息"})
    else:
        sub_From = UserinfoForm(request.POST)
        if sub_From.is_valid():
            sub_From.save()
        return redirect(request, 'sub.html', {'sub_From': sub_From})
