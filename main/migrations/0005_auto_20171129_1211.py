# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20171129_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
