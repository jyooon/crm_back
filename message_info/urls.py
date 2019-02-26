from django.conf.urls import url
from . import views

urlpatterns = [
    url("^create", views.createMessage, name='createMessage'),
    url("^update", views.updateMessage, name='updateMessage'),
    url("^get", views.getMessage, name="getMessage"),
]