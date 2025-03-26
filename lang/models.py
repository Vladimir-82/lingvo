"""Models language identifier."""

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Translate(models.Model):
    """Translate text."""
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата перевода', blank=True, null=True)
    title = models.CharField(max_length=50, verbose_name='Name of translate', blank=True, null=True)
    file_one = models.FileField(upload_to='media', verbose_name='File from translate', blank=True, null=True)
    file_two = models.FileField(upload_to='media', verbose_name='File to translate', blank=True, null=True)
    translate_from_text = models.TextField(verbose_name='Translate from text', blank=True, null=True)
    translated_text = models.TextField(verbose_name='Translated text', blank=True, null=True)
    language_input = models.CharField(max_length=4, verbose_name='Language input', blank=True, null=True)
    language_output = models.CharField(max_length=4, verbose_name='Language output', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('translate', kwargs={"pk": self.pk})

    def __str__(self):
        """Text representation of translate."""
        return self.title
