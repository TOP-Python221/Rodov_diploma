from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Изменённая пользовательская модель, где в качестве уникального идентификационного ключа используется почта вместо имени пользователя.
    """
    def create_user(self, email, password, **extra_fields):
        """Создаёт и сохраняет пользователя с полученной почтой и паролем."""
        if not email:
            raise ValueError('Email должен быть установлен')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """Создаёт и сохраняет суперПользователя с полученной почтой и паролем."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff для СуперПользователя должен быть True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser для СуперПользователя должен быть True')
        return self.create_user(email, password, **extra_fields)

