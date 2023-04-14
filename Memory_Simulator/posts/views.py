from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView

from posts.forms import AddPostForm
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
        context['title'] = 'Главная страница'
        return context


def read_post(request, slug):
    post = get_object_or_404(Posts, slug=slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
    }

    return render(request, 'posts_pages/post.html', context=context)


def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = AddPostForm()

    return render(request, 'posts_pages/post.html ', {'form': form, 'menu': menu, 'title': 'Добавление статьи'
                                                     }
                  )


class AddPost(LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'posts_pages/add_post.html'
    context_object_name = 'add_post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавление статьи'
        return context
