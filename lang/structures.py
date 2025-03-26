"""Auxiliary structures."""

from dataclasses import dataclass


@dataclass
class Language:
    """Auxiliary structures."""

    language: dict
    translate: dict


language = Language(
    {
        'en': 'English',
        'de': 'Deutsch',
        'fr': 'Français',
        'ru': 'Русский',
        'uk': 'Українська',
        'pl': 'Polski',
    },
    {
        'English': 'en',
        'Deutsch': 'de',
        'Français': 'fr',
        'Русский': 'ru',
        'Українська': 'uk',
        'Polski': 'pl',
    },
)
