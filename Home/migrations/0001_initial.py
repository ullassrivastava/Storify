# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-07 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Storify_database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=600)),
                ('writer', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=20)),
            ],
        ),
    ]
