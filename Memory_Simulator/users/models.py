from django.contrib.auth.models import AbstractUser
from django.db import models


class RegUser(AbstractUser):
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Пользователи'
        ordering = ['date_joined']

