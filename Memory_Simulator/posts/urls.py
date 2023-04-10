from django.conf.urls.static import static
from django.urls import path, include

from core import settings
from .views import IndexView, read_post, AddPost

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path("authorize/", include('users.urls'), name='authorize'),
    path("read_post/<int:post_id>", read_post, name='read_post'),
    path("add_post/", AddPost.as_view(), name='add_post'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
