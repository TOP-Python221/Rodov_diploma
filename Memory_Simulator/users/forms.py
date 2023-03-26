from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import *

from users.models import RegUser


class UserRegisterForm(UserCreationForm):
    username = CharField(label='Логин', widget=TextInput())
    email = EmailField(
        help_text='Enter your valid e-mail address.',
        error_messages={
            'invalid': 'Enter a correct e-mail address.',
        }
    )
    password1 = CharField(label='Пароль', widget=PasswordInput())
    password2 = CharField(label='Повторить пароль', widget=PasswordInput())
    email.widget.attrs.update({
        'class': 'input_email'
    })

    class Meta:
        model = RegUser
        fields = ['username', 'email', 'password1', 'password2']
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'input_username',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'input_password1',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'input_password2',
        })
