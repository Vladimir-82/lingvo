"""Auxiliary tools language identifier."""

from io import BytesIO

from django.core.files.base import ContentFile
from googletrans import Translator
from gtts import gTTS

from lang.models import Translate
from lang.structures import language


def get_translate_text(language_to: str, text_for_translate: str) -> tuple[str, str, str]:
    """Get translated_text and language."""
    translate_to = language.translate.get(language_to, 'en')
    translator = Translator()

    translate_from = translator.detect(text_for_translate).lang
    translated = translator.translate(text_for_translate, dest=translate_to)

    return translated.text, translate_from, translate_to


def create_translate_object(
    text_for_translate: str,
    translate_from: str,
    translated_text: str,
    translate_to: str,
) -> Translate:
    """Create translated object."""
    translate_object: Translate = Translate.objects.create()
    object_name = save_title_name(translate_object)

    save_track(text_for_translate, translate_from, translate_object, object_name, 'file_one')
    save_track(translated_text, translate_to, translate_object, object_name, 'file_two')

    translate_object.translate_from_text = text_for_translate
    translate_object.translated_text = translated_text

    translate_object.save()

    return translate_object


def save_track(
    text_to_record: str,
    language_record: str,
    translate_object: Translate,
    object_name: str,
    file_number: str,
) -> None:  # noqa: E501
    """Save track of the translated object."""
    file_1 = record_track(text_to_record=text_to_record, language_record=language_record)
    getattr(translate_object, file_number).save(
        name=''.join((object_name, '_1')),
        content=ContentFile(file_1.getvalue()),
        save=False,
    )


def save_title_name(translate_object: Translate) -> str:
    """Save title name of the translated object."""
    object_name = ''.join(('track', '-', str(translate_object.pk)))
    return translate_object.title


def record_track(text_to_record: str, language_record: str) -> BytesIO:
    """Record text to speak."""
    file_to_record = BytesIO()
    tts = gTTS(text_to_record, lang=language_record)
    tts.write_to_fp(file_to_record)
    return file_to_record
