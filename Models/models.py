from django.db import models

# Create your models here.


class Userinfo(models.Model):
    Name = models.CharField("名字", unique=True, max_length=20)
    User = models.CharField("用户", max_length=20)
    Password = models.CharField("密码", max_length=20)
    Mobile = models.CharField("手机", max_length=20)
    Email = models.CharField("邮件", max_length=20)
    Time = models.DateTimeField("时间", auto_now=True)

    def __str__(self):
        return "[名字] %s [用户] %s [密码] %s [手机] %s [邮件] %s [时间] %s" % (self.Name, self.User, self.Password, self.Mobile, self.Email, self.Time)

    class Meta:
        db_table = "Userinfo"
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name


class Hostinfo(models.Model):
    Hostname = models.CharField("主机名", max_length=20)
    Ip = models.CharField("ip地址", max_length=20)
    Password = models.CharField("密码", max_length=20)
    Cpu = models.CharField("CPU", max_length=20)
    Mem = models.CharField("内存", max_length=20)
    Disk = models.CharField("磁盘", max_length=20)
    Time = models.DateTimeField("时间", auto_now=True)

    def __str__(self):
        return "[主机名] %s [ip地址] %s [密码] %s [CPU] %s [内存] %s [磁盘]%s [时间] %s" % (self.Hostname, self.Ip, self.Password, self.Cpu, self.Mem, self.Disk, self.Time)

    class Meta:
        db_table = "Hostinfo"
        verbose_name = "主机信息"
        verbose_name_plural = verbose_name


class Loginfo(models.Model):
    Messages = models.CharField("消息", max_length=20)
    Time = models.DateTimeField("时间", auto_now=True)

    def __str__(self):
        return "[id] %s [消息] %s [时间] %s" % (self.id, self.Messages, self.Time)

    class Meta:
        db_table = "Loginfo"
        verbose_name = "日志信息"
        verbose_name_plural = verbose_name
