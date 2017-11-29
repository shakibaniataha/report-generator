# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 12:09
from __future__ import unicode_literals

from django.db import migrations, models
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20171126_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='input_params',
            field=models.CharField(blank=True, max_length=200, validators=[main.validators.validate_comma_separated]),
        ),
    ]