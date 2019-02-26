from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from django.http import HttpResponse
from django.http import JsonResponse
import requests
from knox.models import AuthToken
from .serializers import (
    CreateUserSerializer,
    UserSerializer,
    LoginUserSerializer,
)
from django.dispatch import receiver
from user_info.models import Profile
from django.contrib.auth.models import User
# Create your views here.


class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        if len(request.data["username"]) < 6 or len(request.data["password"]) < 4:
            body = {"message": "short field"}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # me = User.objects.get(username=request.data["username"])
        # Profile.objects.create(user_name=request.data["user_name"])
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user),
            }
        )

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        print(request.body)
        # print(request.body['id'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user),
            }
        )


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user