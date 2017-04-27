# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
import hashlib
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mail = models.EmailField(max_length=255)
    role = models.CharField(max_length=1, default='u')
    uid = models.CharField(max_length=255, primary_key=True, editable=False)

    def save(self, silent=False, *args, **kwargs):
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        if self.user.is_superuser:
            self.role = "a"
        if not silent and not self.pk:
            encoded = (timestamp+self.user.email).encode('utf-8')
            self.uid = self.role+"-"+hashlib.sha256(encoded).hexdigest()
        else:
            print ('exists')
            pass
        
        super(Profile, self).save(*args, **kwargs)

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

@receiver(post_save, sender = User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()