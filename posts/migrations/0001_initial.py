# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-13 14:43
from __future__ import unicode_literals

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=3000)),
                ('title', models.CharField(max_length=50)),
                ('video', embed_video.fields.EmbedVideoField(help_text='This is a help text', verbose_name='My video')),
            ],
        ),
    ]
