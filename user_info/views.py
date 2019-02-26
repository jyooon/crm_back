from django.shortcuts import render
from user_info.models import Info
from user_info.models import Profile
# from user_list.models import Profile
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User
# Create your views here.
@csrf_exempt
def info_list(request):
    
    if request.method == 'POST':
        
        data = json.loads(request.body)
    
        # me = Profile.objects.get(user_name='park')
       
        # 현재 로그인 되어있는 관리자의 id 값을 받아와야한다.
        n1 = User.objects.get(id=2)

        
        me = data["user_name"]
        Profile.objects.create(user=n1, user_name=me)
        
        age = data["age"]
        sex = data["sex"]
        address = data["address"]
        latitude = data["latitude"]
        hardness = data["hardness"]

        id = Profile.objects.filter(user_name=me).get().id

        Info.objects.create(name=Profile.objects.get(id=id), age=age, sex=sex, address=address, latitude=latitude, hardness=hardness)
        
        response = HttpResponse('success')
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
        return response


    if request.method == 'GET':
        info = Info.objects.get()

        # json_msg = json.dumps({})
        json_msg = {
            "id" : info.id,
            "name" : me,
            "age" : age,
            "sex" : sex,
            "telegramID" : telegramID,
            "kakaoID" : kakaoID,
            "lineID" : lineID,
            "address" : address,
            "latitude" : latitude,
            "hardness" : hardness
        }
        # print(json_msg)
        
        response = JsonResponse(json_msg)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
        return response

    if request.method == 'PUT':
        data = json.loads(request.body)

        info = Info.objects.get(id=data['id'])
        info.name = data['name']
        info.age = data['age']
        info.sex = data['sex']
        info.telegramID = data['telegramID']
        info.kakaoID = data['kakaoID']
        info.lineID = data['lineID']
        info.address = data['address']
        info.latitude = data['latitude']
        info.hardness = data['hardness']
        info.save()
        response = HttpResponse('success')
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, PUT, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
        return response


    if request.method == 'DELETE':
        # print(request)
        id = json.loads(request.body)['id']
        Info.objects.filter(id=id).delete()
        response = HttpResponse('success')
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, ,DELETE, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
        return response