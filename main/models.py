# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from jsonfield import JSONField
from django.contrib.auth.models import User
from datetime import date
from validators import validate_comma_separated


class API(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    bash_script = models.TextField()
    outputs_dir = models.CharField(max_length=200)
    input_params = models.CharField(max_length=200, validators=[validate_comma_separated]) # This must be a list of comma-separated names (params) as a string


class Request(models.Model):
    REQUEST_STATUS = (
        ('scheduled', 'Scheduled'),
        ('processing', 'Processing'),
        ('finished', 'Finished'),
    )

    api_id = models.ForeignKey(API)
    input_params = JSONField()
    owner = models.ForeignKey(User, null=True)
    preferred_run_date = models.DateField(default=date.today)
    status = models.CharField(max_length=20, choices=REQUEST_STATUS, null=True)