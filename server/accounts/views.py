from django.shortcuts import render
from .models import User

def RegisterUser(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name", "default value")
        LastName = request.POST.get("last_name", "default value")
        Username = request.POST.get("username", "default value")
        Email = request.POST.get("email", "default value")
        Password1 = request.POST.get("password", "default value")
        Password2= request.POST.get("password1", "default value")
        status = request.POST.get("status", 'default value')
        birthday = request.POST.GET("birthday", "default value")
        user = User(first_name = first_name, last_name = LastName, username = Username, email = Email, status = status, birthday =  birthday)
        user.set_password(Password1)
        user.save()
        return render(request, "registration/index.html")
    else:
        return render(request, "registration/register.html", {})