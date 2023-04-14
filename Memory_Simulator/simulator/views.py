from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView

from simulator.forms import InvisibleForm
from simulator.models import Game
from simulator.utils import Mixin, menu


class StatisticsView(Mixin, ListView):
    model = Game
    template_name = 'pages/statistics.html'
    context_object_name = 'stat'
    success_url = reverse_lazy('statistics')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

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


def first_trainer(request):
    global scores
    if request.method == 'POST':
        form = InvisibleForm(request.POST)
        if form.is_valid():
            # try:
            form.save()
            return redirect('couple')
            # except:
            #     form.add_error(None, 'Ошибка записи')
    elif request.method == 'POST':
        form = InvisibleForm(request.POST)
        if form.is_valid():
            scores = form.cleaned_data['scores']
            return scores
    else:
        form = InvisibleForm()
    return render(
        request,
        'pages/first_trainer.html',
        {'form': form, 'menu': menu, 'title': 'Найди пару'}
    )
