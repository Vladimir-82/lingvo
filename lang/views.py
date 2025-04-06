"""Views."""

import logging
import os

from django.contrib import (
    messages,
)
from django.contrib.auth import (
    login,
    logout,
)
from django.core.handlers.wsgi import (
    WSGIRequest,
)
from django.http import (
    Http404,
    HttpResponse,
)
from django.shortcuts import (
    redirect,
    render,
)
from django.views.generic import DeleteView

from exceptions import (
    LimitReportException,
)
from lang.compare import (
    get_document,
)

from .forms import (
    UserLoginForm,
    UserRegisterForm,
)
from .messanges import (
    Message,
)
from .models import (
    Translate,
)
from .structures import (
    Language,
)
from .translate import (
    create_translate_object,
    get_translate_data,
)

logger = logging.getLogger(__name__)


def translates(request):
    """Получение всех переводов пользователя."""
    logger.info('Пользователь %s инициирует получение всех своих переводов' % request.user.username)
    translates = Translate.objects.filter(author=request.user).select_related('author')
    context = {}
    if translates:
        context['translates'] = translates
    else:
        context['message'] = Message.no_translates
    return render(request, 'lang/translates.html', context=context)


def translate_detail(request, pk):
    """Перевод пользователя.

    Только для автора перевода.
    """
    try:
        translate_item = Translate.objects.get(pk=pk)
    except Translate.DoesNotExist:
        raise Http404
    if request.user == translate_item.author:
        return render(request, 'lang/translate_detail.html', {"translate_item": translate_item})
    raise Http404


class DeleteTranslateView(DeleteView):
    """Удаление перевода."""

    model = Translate
    template_name = 'lang/translate_delete.html'
    success_url = '/translates/'


def translate_text(request: WSGIRequest) -> HttpResponse:
    """Перевод текста."""
    if request.user.is_authenticated:
        logger.info('Пользователь %s инициирует перевод текста' % request.user.username)
        if request.method == 'POST':
            request_data = request.POST

            text_for_translate = request_data['text_for_translate']
            language_to = request_data['languages']

            translated_text, language_input, language_output = get_translate_data(language_to, text_for_translate)

            translate_object = create_translate_object(
                text_for_translate,
                language_input,
                translated_text,
                language_output,
                request,
            )

            language_input = Language.language.get(language_input)
            language_output = Language.language.get(language_output)
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


def download_mp3(request, *args, **kwargs):
    """Скачивание mp3 файла.

    Только для автора перевода.
    """
    translate_id = kwargs.get('pk')
    file = kwargs.get('file')
    logger.info('Пользователь %s инициирует скачивание mp3 файла' % request.user.username)
    try:
        translate = Translate.objects.get(pk=translate_id)
    except Translate.DoesNotExist:
        logger.exception('Ошибка при скачивании mp3 файла')
        raise Http404
    if translate.author == request.user:
        path = translate.get_file_1_name() if file == 'file_1' else translate.get_file_2_name()
        file_path = os.path.join('media', path)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                response = HttpResponse(file.read(), content_type="application/vnd.ms-excel")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
    logger.exception('Ошибка при скачивании mp3 файла')
    raise Http404


def compare(request, *args, **kwargs):
    """Скачивание docx файла для сравнения текста и перевода.

    Только для автора перевода.
    """
    logger.info('Пользователь %s инициирует скачивание сравнения перевода текста в Word' % request.user.username)
    translate_id = kwargs.get('pk')
    try:
        translate = Translate.objects.get(pk=translate_id)
    except Translate.DoesNotExist:
        logger.exception('Ошибка при скачивании сравнения перевода текста в Word')
        raise Http404
    if translate.author == request.user:
        try:
            document, file_name = get_document(translate_id)
        except LimitReportException():
            logger.exception('Ошибка при скачивании сравнения перевода текста в Word')
            raise Http404
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = f'attachment; filename={file_name}.docx'
        document.save(response)
        return response
    logger.exception('Ошибка при скачивании сравнения перевода текста в Word')
    raise Http404
