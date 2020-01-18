from django import forms
from Models.models import *

from django.forms import widgets as wid


class UserinfoForm(forms.ModelForm):
    class Meta:
        # 用来指定表格用哪个Model
        model = Userinfo
        # 字段，如果是__all__,就是表示列出所有的字段 ['mood','nickname','message','del_pass',]#指定使用那些字段
        fields = "__all__"
        # 自定义错误信息
        error_messages = None
        # 排除的字段
        exclude = None
        # 提示信息
        labels = None
        # 帮助提示信息
        help_texts = None
        # 自定义属性
        widgets = None

        error_messages = {
            'name': {'required': "用户名不能为空", },
            'age': {'required': "年龄不能为空", },
        }
        widgets = {
            "name": wid.Textarea(attrs={"class": "c1"})
        }
        labels = {
            "name": "用户名"
        }


class HostinfoForm(forms.ModelForm):
    class Meta:
        # 用来指定表格用哪个Model
        model = Hostinfo
        # 字段，如果是__all__,就是表示列出所有的字段 ['mood','nickname','message','del_pass',]#指定使用那些字段
        fields = "__all__"
        # 自定义错误信息
        error_messages = None
        # 排除的字段
        exclude = None
        # 提示信息
        labels = None
        # 帮助提示信息
        help_texts = None
        # 自定义属性
        widgets = None

        error_messages = {
            'name': {'required': "用户名不能为空", },
            'age': {'required': "年龄不能为空", },
        }
        widgets = {
            "name": wid.Textarea(attrs={"class": "c1"})
        }
        labels = {
            "name": "用户名"
        }
