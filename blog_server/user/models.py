from django.db import models

# Create your models here.


class UserProfile(models.Model):
    username=models.CharField("用户名",max_length=30,primary_key=True)
    nickname=models.CharField("昵称",max_length=30,null=False)
    email=models.EmailField("邮箱",max_length=50,null=False)
    password=models.CharField("密码",max_length=40)
    sign=models.CharField("个人签名",max_length=50)
    info=models.CharField("个人描述",max_length=150)
    avatar=models.ImageField("头像",upload_to="avatar/")

    class Meta:
        db_table="user_profile"


