"""Configuration for pytest."""

import datetime

import pytest

from lang.models import (
    Translate,
)


@pytest.fixture
def translate():
    """Создание экземпляра перевода."""
    return Translate(
        id=1,
        created_at=datetime.datetime(year=2020, month=1, day=1, hour=1, minute=1, second=1),
        title='Test_title',
        translate_from_text='test',
        translated_text='тест',
        language_input='en',
        language_output='ua',
    )
