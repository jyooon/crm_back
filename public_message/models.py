from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
# from user_list.models import Profile
# Create your models here.

class Public_Message(models.Model):
    msg1 = models.TextField(max_length=100,null=False, blank=False)
    msg2 = models.TextField(max_length=100,null=False, blank=False)
    msg3 = models.TextField(max_length=100,null=False, blank=False)
    msg4 = models.TextField(max_length=100,null=False, blank=False)
    msg5 = models.TextField(max_length=100,null=False, blank=False)
    msg6 = models.TextField(max_length=100,null=False, blank=False)
    msg7 = models.TextField(max_length=100,null=False, blank=False)
    msg8 = models.TextField(max_length=100,null=False, blank=False)
    msg9 = models.TextField(max_length=100,null=False, blank=False)
    msg10 = models.TextField(max_length=100,null=False, blank=False)
    # img1 = models.ImageField(blank=True)
    # img2 = models.ImageField(blank=True)
    # class Meta:
    #     ordering = ('-name',)
    

