from django.shortcuts import render
from reserve_info.models import Reserve
from user_info.models import Profile
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import pprint
# Create your views here.
@csrf_exempt
def addSchedule(request):
    if request.method == 'POST': 
        data = json.loads(request.body)    
        # id 는 profile 아이디
        pprint.pprint(data)
        # id = data['data']['id']

        me = Profile.objects.get(id=1)
        booker = data['data']["Booker"]
        start_time = data['data']["StartDate"]
        end_time = data['data']["endDate"]
        cost = data['data']["price"]
        memo = data['data']["Memo"]

        Reserve.objects.create(name=me, booker=booker, start_time=start_time, end_time=end_time, cost=cost, memo=memo)
        
        response = HttpResponse('success')
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
        return response


# @csrf_exempt
# def deleteSchedule(request):
#     if request.method == 'DELETE':
#         data = json.loads(request.body)
#         # 삭제할 예약의 아이디
#         # id = data['data']['id']
#         Reserve.objects.filter(id=5).delete()
        
#         response = HttpResponse('delete success')
#         response["Access-Control-Allow-Origin"] = "*"
#         response["Access-Control-Allow-Methods"] = "GET, POST, DELETE, OPTIONS"
#         response["Access-Control-Max-Age"] = "1000"
#         response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
#         return response

# @csrf_exempt
# def updateSchedule(request):
#     if request.method == 'PUT':
#         data = json.loads(request.body)
#         # 업데이트 할 예약의 아이디
#         id = data['data']['id']
#         if 현재 Profile id != 수정한 Profile id:
#             me = Profile.objects.get(id=수정한 Profile id)
#             booker = data['data']["booker"]
#             start_time = data['data']["start_time"]
#             end_time = data['data']["end_time"]
#             cost = data['data']["cost"]
#             memo = data['data']["memo"]
#             Reserve.objects.create(name=me, booker=booker, start_time=start_time, end_time=end_time, cost=cost, memo=memo)

#         else:
#             r1 = Reserve.objects.get(id=id)
#             r1.me = data['data']['me']
#             r1.booker = data['data']['booker']
#             r1.manager = data['data']['manager']
#             r1.start_time = data['data']['start_time']
#             r1.end_time = data['data']['end_time']
#             r1.cost = data['data']['cost']
#             r1.memo = data['data']['memo']
#             r1.save()

#         response = HttpResponse('success')
#         response["Access-Control-Allow-Origin"] = "*"
#         response["Access-Control-Allow-Methods"] = "GET, POST, DELETE, OPTIONS"
#         response["Access-Control-Max-Age"] = "1000"
#         response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
#         return response