from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Register

class UserForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email =  forms.EmailField()
    username = forms.CharField()
    status = forms.CharField(widget=forms.Select(choices = Register.STATUS_CHOICES))
    password = forms.CharField(widget = forms.PasswordInput())
    password1 = forms.CharField(widget = forms.PasswordInput())

    class Meta:
        model = Register
        fields = ["first_name", "last_name", "email", "username", "status", "password", "password1",]