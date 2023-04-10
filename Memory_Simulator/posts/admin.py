from django.contrib import admin
from .models import *


class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('time_create', )


admin.site.register(Posts, PostsAdmin)
