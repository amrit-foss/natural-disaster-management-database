# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-31 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etv', '0003_remove_earthquake_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='earthquake',
            name='country',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='earthquake',
            name='place',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
