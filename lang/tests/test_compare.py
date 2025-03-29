"""Тестирование функций выгрузки текстов в Word и их сравнение."""

from unittest import mock

import pytest

from lang import compare
from lang.compare import (
    get_translate,
    get_file_name,
)


def test_get_translate(translate):
    """Тестирование функции get_translate."""
    with mock.patch.object(compare, 'get_translate_instance', return_value=translate):
        result = get_translate(translate_id=translate.id)

        assert result.get('language_input') == translate.language_input
        assert result.get('language_output') == translate.language_output
        assert result.get('translate_from_text') == translate.translate_from_text
        assert result.get('translated_text') == translate.translated_text
        assert result.get('date') == translate.created_at.strftime('%d.%m.%Y %H:%M')


@pytest.mark.parametrize(
    'translate_data, name',
    [
        ({'translate_from_text': 'This text'}, 'This text'),
        ({'translate_from_text': 'This text is example'}, 'This text is ex'),
        ({'translate_from_text': ''}, ''),
    ]
)
def test_get_file_name_OK(translate_data, name):
    """Тестирование функции get_translate. OK."""
    assert get_file_name(translate_data) == name


@pytest.mark.parametrize(
    'translate_data',
    [
        ({'translate_from_text': None}),
        ({'translate_from_text': 42}),
        ({'translate_from_text': object}),
    ]
)
def test_get_file_name_error(translate_data):
    """Тестирование функции get_translate. Error."""
    with pytest.raises(TypeError):
        assert get_file_name(translate_data)
