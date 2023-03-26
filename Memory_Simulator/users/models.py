from django.contrib.auth.models import User, AbstractUser
from django.db import models

from users.manager import CustomUserManager


class RegUser(AbstractUser):
    email = models.EmailField('email address', unique=True)
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_visit = models.DateTimeField(auto_now=True, verbose_name='Последнее посещение')

    objects = CustomUserManager

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


    class Meta:
        verbose_name_plural = 'Пользователи'
        ordering = ['time_registration']


# КОММЕНТАРИЙ: наследование от класса User возможно (точнее, необходимо наследоваться от AbstractUser), но это требует дополнительного указания для фреймворка о необходимости использовать для авторизации и аутентификации ваш класс, а не встроенный: AUTH_USER_MODEL = RegUser
#   см. https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#substituting-a-custom-user-model

# КОММЕНТАРИЙ: альтернативой является использование агрегации вместо наследования, то есть связь собственного класса для пользователя со встроенным с помощью models.OneToOneField
#   см. https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#extending-the-existing-user-model

