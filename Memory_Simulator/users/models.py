from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, UserManager
from django.db import models
from django.utils import timezone

# from .manager import CustomUserManager


class RegUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=55, blank=True, null=True)
    email = models.EmailField('email address', unique=True)
    age = models.PositiveSmallIntegerField(verbose_name='Возраст', blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_visit = models.DateTimeField(auto_now=True, verbose_name='Последнее посещение')  # УДАЛИТЬ
    date_joined = models.DateTimeField(default=timezone.now)

    # objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name_plural = 'Пользователи'
        ordering = ['date_joined']

    def __str__(self):
        return self.email
