from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView

from simulator.models import Game
from simulator.utils import Mixin

menu = [
    {'title': 'Статистика', 'url_name': 'statistics'},
    {'title': 'Рейтинги', 'url_name': 'ratings'},
    {'title': 'Тренажеры', 'url_name': 'simulators'},
    {'title': 'Авторизация', 'url_name': 'authorization'}
]


class IndexView(ListView):
    model = Game
    template_name = 'pages/main.html'
    context_object_name = 'menu'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['menu'] = menu
        return context


class StatisticsView(Mixin, ListView):
    model = Game
    template_name = 'pages/statistics.html'
    context_object_name = 'stat'
    success_url = reverse_lazy('statistics')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        c_def = self.get_user_context(title='Статистика')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)


class RatingsView(Mixin, ListView):
    model = Game
    template_name = 'pages/ratings.html'
    context_object_name = 'rate'
    success_url = reverse_lazy('ratings')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        c_def = self.get_user_context(title='Рейтинги')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)


def first_trainer(request):
    return render(
        request,
        'pages/first_trainer.html'
    )

