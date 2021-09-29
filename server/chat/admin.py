from django.contrib import admin

from .models import PrivateMessage

class PrivateMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'timestamp', 'is_read')

admin.site.register(PrivateMessage, PrivateMessageAdmin)