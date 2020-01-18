from django.contrib import admin

# Register your models here.
from Models.models import *

admin.site.register([
    Userinfo,
    Hostinfo,
    Loginfo

])
