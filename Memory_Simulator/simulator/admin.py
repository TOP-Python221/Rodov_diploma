from django.contrib import admin

from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'age',
                    'time_registration', 'last_visit', 'is_online',)
    list_display_links = ('id', 'name')
    search_fields = ('name', 'is_online')

admin.site.register(User, UserAdmin)
