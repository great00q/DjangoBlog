# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-27 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0003_remove_article_commentnum'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='commentNum',
            field=models.CharField(default=0, max_length=8),
        ),
    ]