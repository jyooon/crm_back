from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.info_list, name='info_list'),
]