from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]