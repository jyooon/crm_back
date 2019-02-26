from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.reserve_list, name='reserve_list'),
]