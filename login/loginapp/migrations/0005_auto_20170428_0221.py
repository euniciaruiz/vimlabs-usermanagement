# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 02:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0004_auto_20170428_0129'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': (('admin', 'Administrator'), ('manager', 'Manager'), ('user', 'User'))},
        ),
    ]
