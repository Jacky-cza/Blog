from django.http import JsonResponse


def test_api(request):
    #JsonResponse:
    #1.将返回的内容序列化为json
    #2.response
    return JsonResponse({"code":200})