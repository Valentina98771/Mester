from django.urls import path
from django.contrib import admin
from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

app_name = 'profileClient'

urlpatterns = [
    path('user/', views.UserEdit.as_view(), name='userEdit'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),

]