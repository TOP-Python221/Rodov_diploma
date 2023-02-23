from django.shortcuts import render


menu = [{'title': 'Статистика', 'url_name': 'statistics'},
        {'title': 'Рейтинги', 'url_name': 'ratings'},
        {'title': 'Тренажеры', 'url_name': 'simulators'},
        {'title': 'Авторизация', 'url_name': 'authorization'}
        ]

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
