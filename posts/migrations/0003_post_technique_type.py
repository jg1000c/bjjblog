# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-13 19:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20180113_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='technique_type',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
