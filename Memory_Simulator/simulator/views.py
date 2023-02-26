from django.shortcuts import render


# ИСПОЛЬЗОВАТЬ: возможно создать словарь с доступом к ключам с помощью атрибуции

class DictAttr(dict):
    def __getattribute__(self, item):
        return self[item]

menu = [
    DictAttr({'title': 'Статистика', 'url_name': 'statistics'}),
    DictAttr({'title': 'Рейтинги', 'url_name': 'ratings'}),
    DictAttr({'title': 'Тренажеры', 'url_name': 'simulators'}),
    DictAttr({'title': 'Авторизация', 'url_name': 'authorization'})
]

# {% for item in menu %}
#   <a href="{{ item.url }}">{{ item.title }}</a>
# {% endfor %}


def index_view(request):
    return render(
        request,
        'pages/main.html',
        {'title': 'Тренажеры', 'menu': menu}
    )

def login_view(request):
    return render(
        request,
        'pages/login.html',
        {'title': 'Авторизация'}
    )

def registration_view(request):
    return render(
        request,
        'pages/registration.html',
        {'title': 'Регистрация'}
    )


def game_view(request):
    if request.method == 'GET':
        return render(
            request,
            '',
            {}
        )
    elif request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            scores = form.cleaned_data['scores']
            # ...
