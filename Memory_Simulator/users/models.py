from django.contrib.auth.models import User, AnonymousUser
from django.db import models


#КОММЕНТАРИЙ: без связки с имеющейся моделью в приложении auth?
class RegUser(User):
    name = models.CharField(max_length=30, verbose_name='Имя')
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    # ИСПОЛЬЗОВАТЬ: в модели ограничение задаётся только типом поля
    # КОММЕНТАРИЙ: если необходимо добавить дополнительное ограничение, то мы его вводим для соответствующего поля формы с помощью параметров min_value и max_value
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')
    time_registration = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    last_visit = models.DateTimeField(auto_now=True, verbose_name='Последнее посещение')
    is_online = models.BooleanField(default=False, verbose_name='В сети')

    class Meta:
        verbose_name_plural = 'Пользователи'
        ordering = ['time_registration']