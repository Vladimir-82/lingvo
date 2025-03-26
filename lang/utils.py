"""Auxiliary tools language identifier."""

from io import BytesIO

from django.core.files.base import ContentFile
from django.core.handlers.wsgi import WSGIRequest
from googletrans import Translator
from gtts import gTTS

from lang.models import Translate
from lang.structures import language


def get_translate_text(language_to: str, text_for_translate: str) -> tuple[str, str, str]:
    """Получение переведенного текста и языка."""
    translate_to = language.translate.get(language_to, 'en')
    translator = Translator()

    translate_from = translator.detect(text_for_translate).lang
    translated = translator.translate(text_for_translate, dest=translate_to)

    return translated.text, translate_from, translate_to


def create_translate_object(
    text_for_translate: str,
    language_input: str,
    translated_text: str,
    language_output: str,
    request: WSGIRequest,
) -> Translate:
    """Создание объекта перевода."""
    translate_object: Translate = Translate.objects.create()

    translate_object.author = request.user
    title = get_title_name(text_for_translate)
    translate_object.title = title

    save_track(text_for_translate, language_input, translate_object, 'file_one')
    save_track(translated_text, language_output, translate_object, 'file_two')

    translate_object.translate_from_text = text_for_translate
    translate_object.translated_text = translated_text

    translate_object.language_input = language_input
    translate_object.language_output = language_output

    translate_object.save()

    return translate_object


def save_track(
    text_to_record: str,
    language: str,
    translate_object: Translate,
    file_number: str,
) -> None:  # noqa: E501
    """Сохранение трека в БД."""
    track = record_track(text_to_record=text_to_record, language_record=language)
    getattr(translate_object, file_number).save(
        name=file_number,
        content=ContentFile(track.getvalue()),
        save=False,
    )


def get_title_name(text_for_translate: str) -> str:
    """Получение названия перевода."""
    return ''.join((text_for_translate[:40], '...')) if len(text_for_translate) > 40 else text_for_translate


def record_track(text_to_record: str, language_record: str) -> BytesIO:
    """Запись трека."""
    file_to_record = BytesIO()
    tts = gTTS(text_to_record, lang=language_record)
    tts.write_to_fp(file_to_record)
    return file_to_record
