from django import forms

from users.models import RegUser
from .models import *


class LoginUserForm(forms.ModelForm):
    class Meta:
        model = RegUser
        fields = '__all__'


class InvisibleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Game
        fields = ['scores', 'time']
        widgets = {
            'scores': forms.NumberInput(attrs={'id': 'clicks-field'}),
            'time': forms.NumberInput(attrs={'id': 'time'})
        }
