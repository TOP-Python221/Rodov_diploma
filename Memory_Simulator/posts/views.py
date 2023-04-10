from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
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
        context['menu'] = menu
        context['posts'] = posts
        return context


def read_post(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
    }

    return render(request, 'posts_pages/post.html', context=context)


class AddPost(ListView):
    model = Posts
    template_name = 'posts_pages/add_post.html'
    context_object_name = 'add_post'
