from typing import Set

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from simulator.models import Game
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import RegUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = RegUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None,
         {'classes': ('wide',),
          'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    readonly_fields = [
        'date_joined',
    ]
    actions = [
        'activate_users',
    ]

    # Запрет пользователям, не являющимся суперпользователями, предоставлять права суперпользователя.
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()  # type: Set[str]

        if not is_superuser:
            disabled_fields |= {
                'username',
                'is_superuser',
                # Предоставление разрешений только с помощью групп
                # 'user_permissions',
            }

        # Запретить пользователям, не являющимся суперпользователями,
        # редактировать свои собственные разрешения.
        if (
                not is_superuser
                and obj is not None
                and obj == request.user
        ):
            disabled_fields |= {
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            }

        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True

        return form

    # Запрет штатным пользователям удалять экземпляр модели, независимо от их разрешений.
    def has_delete_permission(self, request, obj=None):
        return False

    # Ограничение доступа к настраиваемым действиям.
    def activate_users(self, request, queryset):
        cnt = queryset.filter(is_active=False).update(is_active=True)
        self.message_user(request, 'Activated {} users.'.format(cnt))
        activate_users.short_description = 'Activate Users'  # type: ignore

    # Скрыть activate_users() от пользователей без разрешения на изменение, переопределить get_actions().
    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.has_perm('auth.change_user'):
            del actions['activate_users']

        return actions


# admin.site.unregister(User)
admin.site.register(RegUser, CustomUserAdmin)
