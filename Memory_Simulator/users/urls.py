from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views import RegisterView, logout_user

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', logout_user, name="logout"),
]