# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-27 08:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0005_auto_20180527_1636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='commtentNum',
            new_name='commentNum',
        ),
    ]
