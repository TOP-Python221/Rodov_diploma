from django.contrib.auth import logout, get_user_model, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView

from simulator.utils import Mixin
from users.forms import UserRegisterForm
from django.contrib.auth.models import User

from users.models import RegUser


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)


def login_view(request):
    return render(
        request,
        'registration/login.html',
        {'title': 'Авторизация'}
    )


def logout_view(request):
    logout(request)
    return redirect('/')
