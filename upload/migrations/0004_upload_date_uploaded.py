# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-24 11:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_auto_20160723_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='date_uploaded',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
