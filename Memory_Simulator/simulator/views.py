from django.shortcuts import render

def index_view(request):
    return render(
        request,
        'pages/main.html'
    )

def login_view(request):
    return render(
        request,
        'pages/login.html'
    )
