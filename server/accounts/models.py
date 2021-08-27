from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    status = models.CharField(max_length=100, default = "Nu exista")
    birthday = models.DateField(auto_now=False, null=True, blank=True)
    avatar = models.ImageField(null = True, blank = True)





    