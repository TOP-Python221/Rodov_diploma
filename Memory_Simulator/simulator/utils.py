from .models import *

menu = [{'title': 'Статистика', 'url_name': 'statistics'},
        {'title': 'Рейтинги', 'url_name': 'ratings'},
        {'title': 'Тренажеры', 'url_name': 'simulators'},
        {'title': 'Авторизация', 'url_name': 'authorization'}
        ]

class Mixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        users = User.objects.all()
        rate = Game.objects.all()
        context['menu'] = menu
        context['users'] = users
        context['rate'] = rate
        return context
