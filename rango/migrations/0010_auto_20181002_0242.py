# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-02 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0009_auto_20181002_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilegreetedbyactiveuser',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AlterField(
            model_name='profilelikedbyactiveuser',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]