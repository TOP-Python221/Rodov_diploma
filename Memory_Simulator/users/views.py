from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView

from users.forms import UserRegisterForm
from django.contrib.auth.models import User

from users.models import RegUser


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        users = RegUser.objects.all()
        context['users'] = users
        return context


def logout_user(request):
    logout(request)
    return redirect('login')


















