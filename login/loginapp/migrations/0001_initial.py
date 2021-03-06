# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 05:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('mail', models.EmailField(max_length=255)),
                ('role', models.CharField(default='u', max_length=1)),
                ('uid', models.CharField(editable=False, max_length=255, primary_key=True, serialize=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
