from django.db import models
from django.conf import settings
from django.urls import reverse

class Post(models.Model):
    user  = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete= models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('list')

