from django.db import models

class Admin(models.Model):
    """管理员账户管理"""
    username=models.CharField(verbose_name="用户名",max_length=32)
    password=models.CharField(verbose_name="密码", max_length=64)
    def __str__(self):
        return self.username