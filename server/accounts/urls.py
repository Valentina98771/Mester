from django.urls import path
from . import views

from .views import register

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path("password_reset", views.password_reset_request, name="password_reset"),


]