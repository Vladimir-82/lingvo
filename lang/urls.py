"""urls."""

from django.conf import (
    settings,
)
from django.conf.urls.static import (
    static,
)
from django.urls import (
    path,
)

from .views import (
    DeleteTranslateView,
    compare,
    download_mp3,
    register,
    translate_text,
    user_login,
    user_logout,
    translate_detail,
    translates,
)

urlpatterns = [
    path('', translate_text, name='index'),
    path('translates/', translates, name='translates'),
    path('translate/<int:pk>/', translate_detail, name='translate'),
    path('delete/<int:pk>/', DeleteTranslateView.as_view(), name='delete_translate'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('download_mp3/<int:pk>/<file>/', download_mp3, name='download_mp3'),
    path('compare/<int:pk>/', compare, name='compare'),
] + (
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
