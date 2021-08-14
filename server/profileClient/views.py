from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, request
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm, EditUserForm
from django.contrib.auth            import authenticate, login
from django.views import generic

from django.contrib.auth import get_user_model

User = get_user_model()

def UserEdit(request):
	if request.method == "POST":
		user_form = EditUserForm(request.POST, instance=request.user)
		profile_form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
		if user_form.is_valid():
		    user_form.save()
		elif profile_form.is_valid():
		    profile_form.save()
		return redirect ("profileClient:about")
	user_form = EditUserForm(instance=request.user)
	profile_form = EditProfileForm(instance=request.user.profile)
	return render(request = request, template_name ="index.html", context = {"user":request.user, 
		"user_form": user_form, "profile_form": profile_form })
