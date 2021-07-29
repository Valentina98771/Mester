from django.shortcuts import render
from django.shortcuts import render, redirect
# Create your views here.
from .models import User
from django.db import models
from django.contrib import messages

def RegisterUser(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name", "default value")
        LastName = request.POST.get("last_name", "default value")
        Username = request.POST.get("username", "default value")
        Email = request.POST.get("email", "default value")
        Password1 = request.POST.get("password", "default value")
        Password2= request.POST.get("password1", "default value")
        status = request.POST.get("status", 'default value')
        #if request.POST.get("Password1") == request.POST.get("Password2"):
        user = User(first_name = first_name, last_name = LastName, username = Username, email = Email, status = status)
        user.set_password(Password1)
        user.save()
        return render(request, "registration/index.html")
    else:
        return render(request, "registration/register.html", {})