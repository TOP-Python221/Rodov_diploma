from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import first_trainer, IndexView, StatisticsView, RatingsView

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path("find_a_couple/", first_trainer, name='couple'),
    path("statistics/", StatisticsView.as_view(), name='statistics'),
    path("ratings/", RatingsView.as_view(), name='ratings'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
