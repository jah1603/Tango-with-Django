# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-02 03:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0013_remove_profilelikedbyactiveuser_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilegreetedbyactiveuser',
            name='slug',
        ),
    ]
