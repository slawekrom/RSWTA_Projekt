# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-24 11:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projekt', '0003_auto_20180522_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oferta',
            name='firma',
        ),
        migrations.AddField(
            model_name='oferta',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
