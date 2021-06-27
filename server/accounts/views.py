from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.models import NewUser
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.generic.edit import CreateView

def RegisterUser(request):
    if request.method == "POST":
        FirstName = request.POST.get("FirstName", "default value")
        LastName = request.POST.get("LastName", "default value")
        Username = request.POST.get("Username", "default value")
        Email = request.POST.get("Email", "default value")
        Password = request.POST["Password"]
        Password1= request.POST["Password1"]
        StatusUser = request.POST.get('StatusUser', 'default value')

        if request.POST['Password'] == request.POST['Password1']:
            NewUser(FirstName = FirstName, LastName = LastName, Username = Username, Email = Email, Password = Password, Password1 = Password1, StatusUser = StatusUser).save()
            return render(request, "registration/index.html")
        return render(request, "registration/register.html")
    else:
        return render(request, "registration/register.html")
