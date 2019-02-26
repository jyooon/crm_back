from django.contrib import admin
from django.conf.urls import url, include
from mims.views import RegistrationAPI, LoginAPI, UserAPI


urlpatterns = [
    url('admin/', admin.site.urls),
    url("^auth/register/", RegistrationAPI.as_view()),
    url("^auth/login/", LoginAPI.as_view()),
    url("^auth/user/", UserAPI.as_view()),
    url("^auth/user_info/", include('user_info.urls')),
    url("^message_info/", include('message_info.urls')),
    url("^auth/reserve_info/", include('reserve_info.urls')),
    url("^auth/talk_info/", include('talk_info.urls')),
    url("^auth/public_message/", include('public_message.urls')),
    url("^auth/public_message_get/", include('public_message.urls')),
    url("member/", include('member.urls')),
    url("scheduler/", include('scheduler.urls'))
]
