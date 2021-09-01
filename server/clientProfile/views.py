from django.shortcuts import render, redirect
from .forms import EditProfileForm, EditUserForm
from django.contrib.auth import get_user_model
User = get_user_model()

def UserEdit(request):
	if request.method == "POST":
		user_form = EditUserForm(request.POST, instance=request.user)
		profile_form = EditProfileForm(request.POST, request.FILES, instance=request.user)
		if user_form.is_valid():
		    user_form.save()
		elif profile_form.is_valid():
		    profile_form.save()
		return redirect ("about")
	user_form = EditUserForm(instance=request.user)
	profile_form = EditProfileForm(instance=request.user)
	return render(request = request, template_name ="profile/editProfile.html", context = {"user":request.user, 
		"user_form": user_form, "profile_form": profile_form })