"""Тестирование функций определения языка текста и перевод."""

from io import (
    BytesIO,
)

import pytest

from lang.translate import (
    get_title_name,
    get_translate_data,
    record_track,
)


@pytest.mark.parametrize(
    'language_to, text_for_translate, translate_data',
    [
        ('Русский', 'Text for translate', ('Текст для перевода', 'en', 'ru')),
        ('English', 'Текст для перевода с русского языка', ('Text for translation from Russian', 'ru', 'en')),
        ('', 'Текст для перевода с русского языка', ('Text for translation from Russian', 'ru', 'en')),
        ('Українська', 'Nur Text', ('Тільки текст', 'de', 'uk')),
        ('Français', 'Тільки текст', ('SEULEMENT Texte', 'uk', 'fr')),
        ('Polski', 'Тільки текст', ('Tylko tekst', 'uk', 'pl')),
        ('Deutsch', 'Tylko tekst', ('Nur Text', 'pl', 'de')),
    ]
)
def test_get_translate_data(language_to, text_for_translate, translate_data):
    """Тестирование функции get_translate_data. OK."""
    assert get_translate_data(language_to, text_for_translate) == translate_data


@pytest.mark.parametrize(
    'text, name',
    [
        ('text', 'text'),
        ('В то время некий безымянный печатник создал большую коллекцию размеров и форм шрифтов',
         'В то время некий безымянный печатник соз...'
         ),
        ('', ''),
    ]
)
def test_get_title_name_OK(text, name):
    """Тестирование функции get_title_name. OK."""
    assert get_title_name(text) == name


@pytest.mark.parametrize('text', [None, 42, object])
def test_get_title_name_error(text):
    """Тестирование функции get_title_name. Error."""
    with pytest.raises(TypeError):
        assert get_title_name(text)


def test_record_track_OK():
    """Тестирование функции record_track."""
    file = record_track('some text to translate', 'de')
    assert isinstance(file, BytesIO)


@pytest.mark.parametrize('text, lang', [('Текст для перевода', 'ff'), ('Текст для перевода', 'uu')])
def test_record_track_error(text, lang):
    """Тестирование функции record_track."""
    with pytest.raises(ValueError):
        assert record_track(text, lang)
