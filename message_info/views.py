from django.shortcuts import render
from message_info.models import Message
from user_info.models import Profile
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def createMessage(request):
    
    if request.method == 'POST':
        
        data = json.loads(request.body)

        print(data)
        #profile id
        id = data['id']
        me = Profile.objects.get(id=id)
        msg1 = data['data'][0]['text']
        msg2 = data['data'][1]['text']
        msg3 = data['data'][2]['text']
        msg4 = data['data'][3]['text']
        msg5 = data['data'][4]['text']
        msg6 = data['data'][5]['text']
        msg7 = data['data'][6]['text']
        msg8 = data['data'][7]['text']
        msg9 = data['data'][8]['text']
        msg10 = data['data'][9]['text']
        img1 = data['data'][10]['img']
        img2 = data['data'][11]['img']

        Message.objects.create(name=me, msg1=msg1, msg2=msg2, msg3=msg3, msg4=msg4, msg5=msg5, msg6=msg6, msg7=msg7, msg8=msg8, msg9=msg9, msg10=msg10, img1=img1, img2=img2)
        
        response = HttpResponse('success')
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
        return response

@csrf_exempt
def updateMessage(request):
    if request.method == 'PUT':
        
        data = json.loads(request.body)
        #profile id
        id = data['data']['id']
        message = Message.objects.get(name=Profile.objects.get(id=id))
        message.msg1 = data['data']["msg1"]
        message.msg2 = data['data']["msg2"]
        message.msg3 = data['data']["msg3"]
        message.msg4 = data['data']["msg4"]
        message.msg5 = data['data']["msg5"]
        message.msg6 = data['data']["msg6"]
        message.msg7 = data['data']["msg7"]
        message.msg8 = data['data']["msg8"]
        message.msg9 = data['data']["msg9"]
        message.msg10 = data['data']["msg10"]
        # message.img1 = data['data']["img1"]
        # message.img2 = data['data']["img2"]

        message.save()
        
        
        response = HttpResponse('success')
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
        return response    

@csrf_exempt
def getMessage(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        print(id)
        # 디비 초기화하고나서는 -10 없애기!!!!!!!!!!!!!!!!!!!!!!!!
        id = int(id) - 10
        message = Message.objects.get(id=id)

        # json_msg = json.dumps({})
        json_msg = {
            "Messages":
            [
                {"id": 1, "text": message.msg1},
                {"id": 2, "text": message.msg2},
                {"id": 3, "text": message.msg3},
                {"id": 4, "text": message.msg4},
                {"id": 5, "text": message.msg5},
                {"id": 6, "text": message.msg6},
                {"id": 7, "text": message.msg7},
                {"id": 8, "text": message.msg8},
                {"id": 9, "text": message.msg9},
                {"id": 10, "text": message.msg10},
                # {"id": 11, "img": message.img1},
                # {"id": 12, "img": message.img2}, 
            ]
        }
        
        response = JsonResponse(json_msg, )
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
        return response