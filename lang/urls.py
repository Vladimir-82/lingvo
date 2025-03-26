"""urls language identifier."""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import translate_text, user_login, user_logout, register, TranslatesView, TranslateView, DeleteTranslateView

urlpatterns = [
    path('', translate_text, name='index'),
    path('translates/', TranslatesView.as_view(), name='translates'),
    path('translate/<int:pk>/', TranslateView.as_view(), name='translate'),
    path('delete/<int:pk>/', DeleteTranslateView.as_view(), name='delete_translate'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
] + (
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
