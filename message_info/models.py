from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from user_info.models import Profile
# Create your models here.

class Message(models.Model):
    name = models.OneToOneField(Profile, on_delete=models.CASCADE)
    msg1 = models.TextField(max_length=100,null=True, blank=True)
    msg2 = models.TextField(max_length=100,null=True, blank=True)
    msg3 = models.TextField(max_length=100,null=True, blank=True)
    msg4 = models.TextField(max_length=100,null=True, blank=True)
    msg5 = models.TextField(max_length=100,null=True, blank=True)
    msg6 = models.TextField(max_length=100,null=True, blank=True)
    msg7 = models.TextField(max_length=100,null=True, blank=True)
    msg8 = models.TextField(max_length=100,null=True, blank=True)
    msg9 = models.TextField(max_length=100,null=True, blank=True)
    msg10 = models.TextField(max_length=100,null=True, blank=True)
    img1 = models.ImageField(blank=True)
    img2 = models.ImageField(blank=True)
    # class Meta:
    #     ordering = ('-name',)
