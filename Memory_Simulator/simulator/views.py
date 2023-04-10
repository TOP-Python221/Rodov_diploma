from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from simulator.models import Game
from simulator.utils import Mixin

menu = [
    {'title': 'Статистика', 'url_name': 'statistics'},
    {'title': 'Рейтинги', 'url_name': 'ratings'},
    {'title': 'Тренажеры', 'url_name': 'simulators'},
    {'title': 'Авторизация', 'url_name': 'authorization'}
]


class StatisticsView(Mixin, ListView):
    model = Game
    template_name = 'pages/statistics.html'
    context_object_name = 'stat'
    success_url = reverse_lazy('statistics')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # c_def = self.get_user_context(title='Статистика')
        return context

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)


class RatingsView(ListView):
    model = Game
    template_name = 'pages/ratings.html'
    context_object_name = 'rate'
    success_url = reverse_lazy('ratings')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # c_def = self.get_user_context(title='Рейтинги')
        # return dict(list(context.items()) + list(c_def.items()))
        return context

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)


def login_view(request):
    return render(
        request,
        'registration/login.html',
        {'title': 'Авторизация'}
    )

# def registration_view(request):
#     return render(
#         request,
#         'pages/registration.html',
#         {'title': 'Регистрация'}
#     )


# class FindCouple(Mixin, ListView):
#     model = Game
#     context_object_name = 'game'
#     template_name = 'couple'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         c_def = self.get_user_context(title='Найди Пару')
#         return dict(list(context.items()) + list(c_def.items()))


def first_trainer(request):
    return render(
        request,
        'pages/first_trainer.html'
    )

# def game_view(request):
#     if request.method == 'GET':
#         return render(
#             request,
#             '',
#             {}
#         )
#     elif request.method == 'POST':
#         form = GameForm(request.POST)
#         if form.is_valid():
#             scores = form.cleaned_data['scores']
#             # ...
