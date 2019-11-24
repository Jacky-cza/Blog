import datetime
import json
# Create your views here.
from django.http import JsonResponse

from message.models import Message
from tools.loging_decorator import loging_check
from topic.models import Topic


@loging_check("POST")   #只有登录的才能发送留言，所以要验证权限
def messages(request,topic_id):#为了向message表里面存数据
        """
        留言/回复
        :param request:
        :param topic_id:
        :return:
        """
        if request.method=="POST":
                user=request.user
                json_str=request.body.decode()
                if not json_str:
                        result={"code":402,"error":"please give me json_str"}
                        return JsonResponse(result)
                json_obj=json.loads(json_str)
                content=json_obj.get("content")
                parent_id=json_obj.get("parent_id",0) #parent_id 为回复的留言的id,留言不一定都有回复，所以可能为空，0=false
                if not content:
                        result={"code":403,"error":"please give me content"}
                        return JsonResponse(result)
                now=datetime.datetime.now()
                try:
                        topic=Topic.objects.get(id=topic_id)
                except Exception as e:
                        result = {"code": 404, "error": "the topic is not existed"}
                        return JsonResponse(result)
                if topic.limit=="private":
                        if user.username!=topic.author.username:
                                result = {"code": 405, "error": "please get out ! "}
                                return JsonResponse(result)

                Message.objects.create(content=content,topic=topic,parent_message=parent_id,created_time=now,
                                       publisher=user)
                result={"code":200,"data":{}}
                return JsonResponse(result)



