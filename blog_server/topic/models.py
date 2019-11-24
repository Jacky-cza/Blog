from django.db import models

# Create your models here.
from user.models import UserProfile

#文章的表
class Topic(models.Model):
    title=models.CharField("文章标题",max_length=50)
    category=models.CharField("文章分类",max_length=20)
    limit=models.CharField("文章权限",max_length=10)
    introduce = models.CharField("文章简介", max_length=90)
    content = models.TextField("文章内容")
    created_time=models.DateTimeField("创建时间",auto_created=True)
    modified_time=models.DateTimeField("更改时间",auto_created=True)
    author = models.ForeignKey(UserProfile)

    class Meta:
        db_table = "topic"