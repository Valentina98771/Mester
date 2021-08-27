from django.urls import path
from . import views
from django.views.generic.base import TemplateView

app_name = 'profileClient'

urlpatterns = [
    path('index/', TemplateView.as_view(template_name='index.html'), name='index'),
    path('user/', views.UserEdit, name='user'),
    path('about/', TemplateView.as_view(template_name='profile/about.html'), name='about'),
    path('craftsmen/', TemplateView.as_view(template_name='profile/craftsmen.html'), name='craftsmen'),
    path('photo/', TemplateView.as_view(template_name='profile/photo.html'), name='photo'),

]