"""Админка переводчика."""

from django.contrib import admin

from .models import Translate


@admin.register(Translate)
class TranslateAdmin(admin.ModelAdmin):
    """Админка переводчика."""

    list_display = ('id', 'title', 'author', 'created_at', 'language_input', 'language_output')
    list_display_links = ('id', 'title', 'author')
    search_fields = ('id', 'author__username', 'language_input', 'language_output')
    raw_id_fields = ('author',)
    ordering = ('id',)
