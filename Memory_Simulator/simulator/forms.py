from django import forms
from .models import *


class LoginUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class RegistrationUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'age']

