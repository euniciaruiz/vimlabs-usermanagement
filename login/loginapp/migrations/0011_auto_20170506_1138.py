# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0010_auto_20170505_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
