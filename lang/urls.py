"""urls language identifier."""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index, user_login, user_logout, register

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
] + (
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
