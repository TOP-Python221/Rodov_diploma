from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    email = forms.EmailField(
        help_text='Enter your valid e-mail address.',
        error_messages={
            'invalid': 'Enter a correct e-mail address.',
        }
    )
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повторить пароль', widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
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

