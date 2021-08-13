from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, request
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm
from django.contrib.auth            import authenticate, login
from django.views import generic

from django.contrib.auth import get_user_model

User = get_user_model()

class UserEdit(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'index.html'
    success_url = reverse_lazy('profileClient:about')
    
    def get_object(self):
       return self.request.user