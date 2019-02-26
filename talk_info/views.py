from django.shortcuts import render
from talk_info.models import Talk
from user_info.models import Profile
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def talk_list(request):
    
    if request.method == 'POST':
        
        data = json.loads(request.body)
        me = data["user_name"]
        id = Profile.objects.filter(user_name=me).get().id
        # me = Profile.objects.get(user_name='park')
        talk_type = data["talk_type"]
        talk_name = data["talk_name"]
        talk_age = data["talk_age"]
        deviceID = data["deviceID"]
        
        Talk.objects.create(name=Profile.objects.get(id=id), talk_type=talk_type, talk_name=talk_name, talk_age=talk_age, deviceID=deviceID)
        
        response = HttpResponse('success')
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
        return response


