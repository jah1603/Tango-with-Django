# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-02 03:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0012_auto_20181002_0330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilelikedbyactiveuser',
            name='slug',
        ),
    ]
