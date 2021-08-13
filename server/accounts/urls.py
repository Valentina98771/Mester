from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('', views.RegisterUser, name = 'registerUser'),

]