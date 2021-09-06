from django.shortcuts import render
from .models import User
from django.shortcuts import render, redirect
from .forms import EditProfileForm, EditUserForm
from django.contrib.auth import get_user_model
User = get_user_model()

def RegisterUser(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name", "default value")
        LastName = request.POST.get("last_name", "default value")
        Username = request.POST.get("username", "default value")
        Email = request.POST.get("email", "default value")
        Password1 = request.POST.get("password", "default value")
        Password2= request.POST.get("password1", "default value")
        status = request.POST.get("status", 'default value')
        #birthday = request.POST.GET("birthday", "default value")
        user = User(first_name = first_name, last_name = LastName, username = Username, email = Email, status = status,)
        user.set_password(Password1)
        user.save()
        return render(request, "registration/index.html")
    else:
        return render(request, "registration/register.html", {})

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
	return render(request = request, template_name ="clientProfile/profile/editProfile.html", context = {"user":request.user, 
		"user_form": user_form, "profile_form": profile_form })