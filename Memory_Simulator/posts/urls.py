from django.conf.urls.static import static
from django.urls import path, include

from core import settings
from .views import IndexView, read_post

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path("authorize/", include('users.urls'), name='authorize'),
    path("memo/", include('simulator.urls'), name='memo'),
    path("read_post/<int:post_id>", read_post, name='read_post')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
