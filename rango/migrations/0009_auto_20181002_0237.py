# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-02 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0008_auto_20181002_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilegreetedbyactiveuser',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
        migrations.AddField(
            model_name='profilelikedbyactiveuser',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
