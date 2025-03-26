"""Views language identifier."""

from django.contrib import messages
from django.contrib.auth import (
    logout,
    login,
)
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import (
    render,
    redirect,
)
from django.views import View
from django.views.generic import (
    TemplateView,
    DetailView,
    DeleteView,
)

from .forms import (
    UserLoginForm,
    UserRegisterForm,
)
from .messanges import Message
from .models import Translate

from .structures import language
from .utils import (
    create_translate_object,
    get_translate_text,
)


class TranslatesView(View):
    """Получение всех переводов пользователя."""

    def get(self, request):
        """Получить переводы."""
        translates = Translate.objects.filter(author=request.user).select_related('author')
        context = {}
        context['translates'] = translates
        return render(request, 'lang/translates.html', context=context)


class TranslateView(DetailView):
    """Перевод пользователя."""

    model = Translate
    context_object_name = 'translate_item'


class DeleteTranslateView(DeleteView):
    """Удаление перевода."""

    model = Translate
    template_name = 'lang/translate_delete.html'
    success_url = '/translates/'


def translate_text(request: WSGIRequest) -> HttpResponse:  # noqa: WPS210
    """Перевод текста."""
    if request.user.is_authenticated:
        if request.method == 'POST':
            request_data = request.POST

            text_for_translate = request_data['text_for_translate']
            language_to = request_data['languages']

            translated_text, language_input, language_output = get_translate_text(language_to, text_for_translate)

            translate_object = create_translate_object(
                text_for_translate,
                language_input,
                translated_text,
                language_output,
                request,
            )

            language_input = language.language.get(language_input)
            language_output = language.language.get(language_output)
            translate_data_to_render = {
                'language_input': language_input,
                'text_for_translate': text_for_translate,
                'translate_object': translate_object,
                'translated_text': translated_text,
                'language_output': language_output,
            }
        else:
            translate_data_to_render = {}
    else:
        translate_data_to_render = {'message': Message.unauthorized}
    return render(request, 'lang/main.html', context=translate_data_to_render)


def register(request):
    """Регистрация."""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, Message.success_register)
            return redirect('/')
        else:
            messages.error(request, Message.error_register)
    else:
        form = UserRegisterForm()
    return render(request, 'lang/register.html', {"form": form})


def user_login(request):
    """Авторизация."""
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = UserLoginForm()
    return render(request, 'lang/login.html', {"form": form})


def user_logout(request):
    """Разлогирование."""
    logout(request)
    return redirect('login')
