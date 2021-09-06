from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    status = models.CharField(max_length=100, default = "Nu exista")
    birthday = models.DateField(auto_now=False, null=True, blank=True)
    avatar = models.ImageField(null = True, blank = True)

class Profile(models.Model):
    user   = models.OneToOneField(settings.AUTH_USER_MODEL, null = True, on_delete= models.CASCADE)
    avatar = models.ImageField(default = "default.jpg", upload_to="images", blank=True)
    birthday = models.DateField(auto_now_add = False, null=True, blank=True)

    def __str__(self):
        return str(self.user)




    