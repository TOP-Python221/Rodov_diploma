from django.contrib.auth.models import User
from django.db import models


# ИСПРАВИТЬ: большинство полей, которые вы объявляете в своём классе, уже есть в классе User: они наследуются от AbstractUser — таким образом в таблице, соответствующей классу RegUser, окажутся лишние столбцы, возможно с дублирующимися значениями
class RegUser(User):
    name = models.CharField(max_length=30, verbose_name='Имя')
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')
    time_registration = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    last_visit = models.DateTimeField(auto_now=True, verbose_name='Последнее посещение')
    is_online = models.BooleanField(default=False, verbose_name='В сети')

    class Meta:
        verbose_name_plural = 'Пользователи'
        ordering = ['time_registration']


# КОММЕНТАРИЙ: наследование от класса User возможно (точнее, необходимо наследоваться от AbstractUser), но это требует дополнительного указания для фреймворка о необходимости использовать для авторизации и аутентификации ваш класс, а не встроенный: AUTH_USER_MODEL = RegUser
#   см. https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#substituting-a-custom-user-model

# КОММЕНТАРИЙ: альтернативой является использование агрегации вместо наследования, то есть связь собственного класса для пользователя со встроенным с помощью models.OneToOneField
#   см. https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#extending-the-existing-user-model

