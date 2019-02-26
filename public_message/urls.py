from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.public_message_list, name='public_message_list'),
    # url(r'^$', views.public_message_list_get, name='public_message_list_get'),
]