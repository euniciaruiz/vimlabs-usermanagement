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
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    role = models.CharField(max_length=1, default='u', editable=False)
    uid = models.CharField(max_length=255, primary_key=True, editable=False)

    class Meta:
        permissions = (
            ("admin", "Administrator"),
            ("manager", "Manager"),
            ("user", "User"),
        )

    def save(self, silent=False, *args, **kwargs):
        # admins = Group.objects.get(name='administrators')
        # managers = Group.objects.get(name='managers')
        # users = Group.objects.get(name='users')

        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        if self.user.is_superuser and self.user.is_staff:
            self.role = "a"
        if self.user.is_staff and not self.user.is_superuser:
            self.role = "m"
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