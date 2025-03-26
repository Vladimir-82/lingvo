# Generated by Django 5.1.7 on 2025-03-26 10:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lang', '0002_translate_language_input_translate_language_output_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='translate',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='translate',
            name='file_one',
            field=models.FileField(blank=True, null=True, upload_to='media', verbose_name='File from translate'),
        ),
        migrations.AlterField(
            model_name='translate',
            name='file_two',
            field=models.FileField(blank=True, null=True, upload_to='media', verbose_name='File to translate'),
        ),
        migrations.AlterField(
            model_name='translate',
            name='language_input',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Language input'),
        ),
        migrations.AlterField(
            model_name='translate',
            name='language_output',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Language output'),
        ),
        migrations.AlterField(
            model_name='translate',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Name of translate'),
        ),
        migrations.AlterField(
            model_name='translate',
            name='translate_from_text',
            field=models.TextField(blank=True, null=True, verbose_name='Translate from text'),
        ),
        migrations.AlterField(
            model_name='translate',
            name='translated_text',
            field=models.TextField(blank=True, null=True, verbose_name='Translated text'),
        ),
    ]
