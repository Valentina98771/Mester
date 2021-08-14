from django import forms
from .models import Profile
from django.contrib.auth import get_user_model
User = get_user_model()

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birthday', 'avatar']