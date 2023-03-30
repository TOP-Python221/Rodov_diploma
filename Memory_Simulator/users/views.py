from django.contrib.auth import get_user_model, logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegisterForm


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        users = get_user_model().objects.all()
        context['users'] = users
        return context


def login_view(request):
    return render(
        request,
        'registration/login.html',
        {'title': 'Авторизация'}
    )


def logout_view(request):
    logout(request)
    return redirect('login')

