# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
import hashlib
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
# Create your models here.



class Profile(models.Model):

    ROLES = (
        ('u', 'User'),
        ('m', 'Manager'),
        ('a', 'Administrator')
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=400)
    role = models.CharField(max_length=1, default='u', choices=ROLES)
    uid = models.CharField(max_length=255, primary_key=True, editable=False)


    def save(self, silent=False, *args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        if not silent and not self.pk:
            encoded = (timestamp+self.email).encode('utf-8')
            self.uid = self.role+"-"+hashlib.sha256(encoded).hexdigest()
                
        else:
            pass
        
        super(Profile, self).save(*args, **kwargs)

