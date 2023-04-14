from django.contrib.auth.forms import UserCreationForm, UsernameField, UserChangeForm
from django import forms
from django.contrib.auth import get_user_model

from users.models import RegUser


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput())
    email = forms.EmailField(
        label='Почта',
        help_text='Enter your valid e-mail address.',
        error_messages={
            'invalid': 'Enter a correct e-mail address!',
        }
    )
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повторить пароль', widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'age', 'password1', 'password2']
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'input_username',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'input_email',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'input_password1',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'input_password2',
        })


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = RegUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = RegUser
        fields = ('email',)
