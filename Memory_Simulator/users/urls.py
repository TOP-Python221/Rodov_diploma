import django
from django.contrib.auth.views import LoginView, LogoutView
from django.template.defaulttags import url
from django.urls import path

from simulator.views import login_view
from users.views import RegisterView, logout_view

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', logout_view, name="logout"),
]