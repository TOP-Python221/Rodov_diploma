from django.db import models


# КОММЕНТАРИЙ: без связки с имеющейся моделью в приложении auth?
class User(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    age = models.IntegerField(max_length=3, verbose_name='Возраст')
    time_registration = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    last_visit = models.DateTimeField(auto_now=True, verbose_name='Последнее посещение')
    is_online = models.BooleanField(default=False, verbose_name='В сети')

    class Meta:
        verbose_name_plural = 'Пользователи'
        ordering = ['time_registration']

