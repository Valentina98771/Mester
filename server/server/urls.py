from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='registration/index.html'), name='index'),
    path('select/', TemplateView.as_view(template_name='registration/select.html'), name='select'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('profileClient/', include('django.contrib.auth.urls')),
    path('profileClient/', include('profileClient.urls')),
    path('profileClient/', TemplateView.as_view(template_name='index.html'), name='about'),
    path('posts/', include('posts.urls')),
    path('posts/', include('django.contrib.auth.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

