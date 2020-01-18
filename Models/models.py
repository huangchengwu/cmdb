from django.db import models

# Create your models here.


class Userinfo(models.Model):
    Name = models.CharField(max_length=20)
    User = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    Mobile = models.CharField(max_length=20)
    Email = models.CharField(max_length=20)

    class Meta:
        db_table = "Userinfo"


class Hostinfo(models.Model):
    Hostname = models.CharField(max_length=20)
    Ip = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    Cpu = models.CharField(max_length=20)
    Mem = models.CharField(max_length=20)
    Disk = models.CharField(max_length=20)

    class Meta:
        db_table = "Hostinfo"


class Loginfo(models.Model):
    Messages = models.CharField(max_length=20)
    Time = models.CharField(max_length=20)

    class Meta:
        db_table = "Loginfo"
