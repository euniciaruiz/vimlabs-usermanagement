# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0008_auto_20170505_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
        migrations.AddField(
            model_name='profile',
            name='uid',
            field=models.CharField(default='12ljlfajfl14j08fao', editable=False, max_length=300, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('u', 'User'), ('m', 'Manager'), ('a', 'Administrator')], default='u', max_length=1),
        ),
    ]
