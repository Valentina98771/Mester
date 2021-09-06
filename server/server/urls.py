from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django_private_chat import urls as django_private_chat_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', TemplateView.as_view(template_name='registration/index.html'), name='index'),
    path('select/', TemplateView.as_view(template_name='registration/select.html'), name='select'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('django.contrib.auth.urls')),
    #path('', include('clientProfile.urls')),
    path('', TemplateView.as_view(template_name='clientProfile/index.html'), name='about'),
    path('', include('posts.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('django_private_chat.urls')),
    path('', include('chat.urls')),
    path('', TemplateView.as_view(template_name='base.html'), name='base'),
    url(r'^messages/', include('django_messages.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

