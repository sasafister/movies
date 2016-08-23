# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20160731005009 on 2016-08-18 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(verbose_name='date published')),
            ],
            options={
                'indexes': [],
            },
        ),
    ]