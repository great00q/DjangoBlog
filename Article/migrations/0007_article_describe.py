# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-06 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0006_auto_20180527_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='describe',
            field=models.TextField(default='None'),
        ),
    ]
