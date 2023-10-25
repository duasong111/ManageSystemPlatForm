
from django import forms
from django.core.validators import RegexValidator
from  django.core.exceptions import ValidationError
from App001 import models
from App001.utils.bootstrap import BootStrapModelForm
class UserModelForm(BootStrapModelForm):
    name = forms.CharField(
        min_length=3,
        label="用户名",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age"]