# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0007_delete_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='lafjl@fj.com', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='helo', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='laja', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='password',
            field=models.CharField(default='jlafj', max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default='jalfj', max_length=255),
            preserve_default=False,
        ),
    ]
