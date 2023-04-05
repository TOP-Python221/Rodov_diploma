from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.db import models
from django.utils import timezone

from .manager import CustomUserManager


class RegUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=55, blank=True, null=True)
    email = models.EmailField('email address', unique=True)
    age = models.PositiveSmallIntegerField(verbose_name='Возраст', blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_visit = models.DateTimeField(auto_now=True, verbose_name='Последнее посещение')
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name_plural = 'Пользователи'
        ordering = ['date_joined']

    # def is_authenticated(self):
    #     return True

    def get_is_authenticated(self):
        auth = super().is_authenticated()
        return auth

    def __str__(self):
        return self.email
