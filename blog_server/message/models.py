from django.db import models

# Create your models here.
from topic.models import Topic
from user.models import UserProfile

#定义留言的表
class Message(models.Model):
    topic=models.ForeignKey(Topic)# 哪个文章的留言,  一篇博客文章可以有多个留言 ,关联的主键是博客文章的id
    content = models.CharField("评论内容", max_length=60)
    publisher = models.ForeignKey(UserProfile) #一个用户可以有多个留言  关联的主键是用户名
    #当前内容的父级留言
    parent_message = models.IntegerField("回复的留言的id")
    created_time = models.DateTimeField("创建时间")

    class Meta:
        db_table="message"



