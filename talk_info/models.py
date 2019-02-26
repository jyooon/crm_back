from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from user_info.models import Profile
# Create your models here.

class Talk(models.Model):
    name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    talk_type = models.CharField(max_length=20, null=False, blank=False)
    talk_name = models.CharField(max_length=20, null=False, blank=False)
    talk_age = models.IntegerField(null=False, blank=False)
    deviceID = models.CharField(max_length=100, null=False, blank=False)
    
    class Meta:
        ordering = ('-name',)
    