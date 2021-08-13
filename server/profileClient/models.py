from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this
from django.conf import settings

class Profile(models.Model):
    user   = models.OneToOneField(settings.AUTH_USER_MODEL, null = True, on_delete= models.CASCADE)
    avatar = models.ImageField(null = True, blank = True)
    birthday = models.DateField(auto_now=False, null=True, blank=True)

    def __str__(self):
        return str(self.user)
