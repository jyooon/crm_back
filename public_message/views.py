from django.shortcuts import render
from public_message.models import Public_Message
from user_info.models import Profile
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import pprint
# Create your views here.
@csrf_exempt
def public_message_list(request):
    
    if request.method == 'POST':
        
        pprint.pprint(json.loads(request.body))

        data = json.loads(request.body)

        msg1 = data[0]['text']
        msg2 = data[1]['text']
        msg3 = data[2]['text']
        msg4 = data[3]['text']
        msg5 = data[4]['text']
        msg6 = data[5]['text']
        msg7 = data[6]['text']
        msg8 = data[7]['text']
        msg9 = data[8]['text']
        msg10 = data[9]['text']
        # img1 = data[10]['img']
        # img2 = data[11]['img']


        public_message = Public_Message.objects.get(id='1')
        public_message.msg1 = msg1
        public_message.msg2 = msg2
        public_message.msg3 = msg3
        public_message.msg4 = msg4
        public_message.msg5 = msg5
        public_message.msg6 = msg6
        public_message.msg7 = msg7
        public_message.msg8 = msg8
        public_message.msg9 = msg9
        public_message.msg10 = msg10
        # public_message.img1 = img1
        # public_message.img2 = img2
        public_message.save()
        
        response = HttpResponse('success')
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
        return response

    if request.method == 'GET':
        message = Public_Message.objects.get()

        # json_msg = json.dumps({})
        json_msg = {
            "commonMessages":
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

# def public_message_list_get(request):
