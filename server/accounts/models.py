from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import AbstractUser, User

class User(AbstractUser):
    status = models.CharField(max_length=100)
    birthday = models.DateField(auto_now=False, null=True, blank=True)
    avatar = models.ImageField(null = True, blank = True)





    