"""Configuration for pytest."""

import datetime

import pytest

from lang.models import Translate
from django.contrib.auth.models import User
from mixer.backend.django import mixer


@pytest.fixture
def translate():
    """Создание экземпляра перевода."""
    return mixer.blend(
        Translate,
        id=1,
        author=mixer.blend(User, username='test'),
        created_at=datetime.datetime(year=2020, month=1, day=1, hour=1, minute=1, second=1),
        title='Test_title',
        translate_from_text='test',
        translated_text='тест',
        language_input='en',
        language_output='ua',
    )
