from django.conf.urls import url
from . import views

urlpatterns = [
    # url("^all", views.getMembers, name='getMembers'),
    # url("^update", views.updateInfo, name="updateInfo"),
    url("^add", views.addSchedule, name="addSchedule"),
    # url("^delete", views.deleteSchedule, name="deleteSchedule"),
    # url("^updatestatus", views.updateStatus, name="updateStatus"),
]