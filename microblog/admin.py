from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

admin.site.site_header = 'M+ | Microblogging Done Right'

admin.site.unregister(Group)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body',)
    
admin.site.register(Tag)
admin.site.register(Like)