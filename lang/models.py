"""Models language identifier."""

from django.db import models
from django.contrib.auth.models import User


class Translate(models.Model):
    """Translate text."""
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50, blank=True, verbose_name='Name of translate')
    file_one = models.FileField(upload_to='media', verbose_name='File from translate', blank=True)
    file_two = models.FileField(upload_to='media', verbose_name='File to translate', blank=True)
    translate_from_text = models.TextField(verbose_name='Translate from text', blank=True)
    translated_text = models.TextField(verbose_name='Translated text', blank=True)

    def __str__(self):
        """Text representation of translate."""
        return self.title
