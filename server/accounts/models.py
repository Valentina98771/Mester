from django.db import models

class NewUser(models.Model):
    FirstName = models.CharField(max_length=150)
    LastName = models.CharField(max_length=150)
    Username = models.CharField(max_length=150)
    Email = models.EmailField(max_length=150)
    Password = models.CharField(max_length=150)
    Password1 = models.CharField(max_length=150)
    StatusUser = models.CharField(max_length=150)
    
    USERNAME_FIELD = 'Username'
    REQUIRED_FIELDS = []
    