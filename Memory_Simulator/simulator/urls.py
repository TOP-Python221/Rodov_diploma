from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import first_trainer, StatisticsView, RatingsView

urlpatterns = [
    path("find_a_couple/", first_trainer, name='couple'),
    path("statistics/", StatisticsView.as_view(), name='statistics'),
    path("ratings/", RatingsView.as_view(), name='ratings'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
