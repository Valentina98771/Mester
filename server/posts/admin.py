from django.contrib import admin
from .models import Post 

class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'created_on', 'updated_on')
    
admin.site.register(Post, PostAdmin)