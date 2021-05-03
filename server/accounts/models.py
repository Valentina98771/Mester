from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Register(models.Model):
    first_name = models.CharField(max_length = 128)
    last_name = models.CharField(max_length = 128)
    email = models.EmailField()
    username = models.CharField(max_length = 30)
    STATUS_CHOICES = [
        ('CLIENT', 'Client'),
        ('MESTER', 'Mester'),
    ]
    status = models.CharField(max_length = 6, choices = STATUS_CHOICES)
    password = models.CharField(max_length = 128)
    password1 = models.CharField(max_length = 128)