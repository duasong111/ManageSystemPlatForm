from django.db import models

class UserLogin(models.Model):
    """用户表"""
    name = models.CharField(verbose_name="用户名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=64)
    email=models.CharField(verbose_name="邮箱",max_length=128)
    img = models.CharField(verbose_name="头像", max_length=128)



