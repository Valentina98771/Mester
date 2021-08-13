from django import forms
from django.forms import ModelForm
from .models import Profile
from django.forms import SelectDateWidget

from django.contrib.auth import get_user_model

User = get_user_model()

class EditProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'birthday', 'avatar']