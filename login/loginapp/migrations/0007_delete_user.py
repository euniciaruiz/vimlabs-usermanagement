# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 03:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0006_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
