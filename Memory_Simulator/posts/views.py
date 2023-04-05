from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from posts.models import Posts
from simulator.utils import menu, Mixin
from users.models import RegUser


class IndexView(ListView):
    model = Posts
    template_name = 'posts_pages/main.html'
    context_object_name = 'menu'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        posts = Posts.objects.all()
        user = RegUser.objects.all()
        context['menu'] = menu
        context['posts'] = posts
        context['user'] = user
        return context


def read_post(request, post_id):
    return HttpResponse(f'Читать статью с id = {post_id}')
