# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0009_auto_20170505_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uid',
            field=models.CharField(editable=False, max_length=255, primary_key=True, serialize=False),
        ),
    ]