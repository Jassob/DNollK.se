# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-30 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='ordering',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]