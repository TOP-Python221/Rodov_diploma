from django.contrib.auth import get_user_model

from simulator.models import Game

menu = [
    {'title': 'Статистика', 'url_name': 'statistics'},
    {'title': 'Рейтинги', 'url_name': 'ratings'},
    {'title': 'Тренажеры', 'url_name': 'simulators'},
    {'title': 'Авторизация', 'url_name': 'authorization'},
    {'title': 'Добавление статьи', 'url_name': 'add_post'},
]


class Mixin:
    def get_context_data(self, **kwargs):
        context = kwargs
        users = get_user_model().objects.all()
        rate = Game.objects.all()
        context['menu'] = menu
        context['users'] = users
        context['rate'] = rate
        return context
