from django.urls import path, include
from simulator.views import index_view, login_view, registration_view

urlpatterns = [
    path("", index_view, name='main'),
    path("login/", login_view, name='login'),
    path("registration/", registration_view, name='registration'),
]