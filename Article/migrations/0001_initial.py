# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-25 13:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('status', models.SmallIntegerField(default=0)),
                ('content', models.TextField()),
                ('isTop', models.BooleanField()),
                ('isLock', models.BooleanField()),
                ('postTime', models.DateField(auto_now_add=True)),
                ('commentNum', models.CharField(max_length=8)),
                ('viewNum', models.CharField(max_length=8)),
                ('authorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parentId', models.SmallIntegerField(default=0)),
                ('cateName', models.CharField(max_length=20)),
                ('count', models.SmallIntegerField(default=0)),
                ('order', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parentId', models.SmallIntegerField(default=0)),
                ('content', models.TextField()),
                ('postTime', models.DateField(auto_now_add=True)),
                ('idChecked', models.BooleanField(default=False)),
                ('articleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Article.Article')),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagName', models.CharField(max_length=20)),
                ('count', models.SmallIntegerField(default=0)),
                ('order', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='cateId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Article.Cate'),
        ),
        migrations.AddField(
            model_name='article',
            name='tagId',
            field=models.ManyToManyField(to='Article.Tag'),
        ),
    ]