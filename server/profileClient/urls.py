from django.urls import path
from . import views
from django.views.generic.base import TemplateView

app_name = 'profileClient'

urlpatterns = [
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('user/', views.UserEdit, name='user'),

]