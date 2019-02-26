from django.conf.urls import url
from . import views

urlpatterns = [
    url("^all", views.getMembers, name='getMembers'),
    url("^update", views.updateInfo, name="updateInfo"),
    url("^add", views.addMember, name="addMember"),
    url("^delete", views.deleteMember, name="deleteMember"),
    url("^statusupdate", views.updateStatus, name="updateStatus"),
]