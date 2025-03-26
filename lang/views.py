"""Views language identifier."""

from django.contrib import messages
from django.contrib.auth import logout, login
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm
from .messanges import Message

from .structures import language
from .utils import create_translate_object, get_translate_text


def index(request: WSGIRequest) -> HttpResponse:  # noqa: WPS210
    """Language identifier."""
    if request.user.is_authenticated:
        if request.method == 'POST':
            request_data = request.POST

            text_for_translate = request_data['text_for_translate']
            language_to = request_data['languages']

            translated_text, translate_from, translate_to = get_translate_text(language_to, text_for_translate)

            translate_object = create_translate_object(
                text_for_translate,
                translate_from,
                translated_text,
                translate_to,
                request,
            )

            language_input = language.language.get(translate_from)
            language_output = language.language.get(translate_to)
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
    """Register a new user."""
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
    """Login of service users."""
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
    """Logs out user."""
    logout(request)
    return redirect('login')
