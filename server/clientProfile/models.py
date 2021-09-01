from django.db import models
from django.conf import settings

class Profile(models.Model):
    user   = models.OneToOneField(settings.AUTH_USER_MODEL, null = True, on_delete= models.CASCADE)
    avatar = models.ImageField(default = "default.jpg", upload_to="images", blank=True)
    birthday = models.DateField(auto_now_add = False, null=True, blank=True)

    def __str__(self):
        return str(self.user)
