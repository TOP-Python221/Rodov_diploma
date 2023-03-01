from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import index_view, login_view, registration_view, first_trainer

urlpatterns = [
    path("", index_view, name='main'),
    path("login/", login_view, name='login'),
    path("registration/", registration_view, name='registration'),
    path("first_trainer/", first_trainer, name='first_trainer'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)