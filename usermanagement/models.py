from __future__ import unicode_literals
import datetime
from django.db import models
from django.core.urlresolvers import reverse

def _generateHash():
        return datetime.datetime.now().strftime("%Y%m%d%H%M%S")

# Create your models here

class User(models.Model):
        MANAGER = 'm'
        USER = 'u'

        ROLES = (
                        (MANAGER, 'Manager'), 
                        (USER, 'User'),
                )
        user_name = models.CharField(max_length=200)
        email = models.CharField(max_length=200)
        role = models.CharField(max_length=1, choices=ROLES, null=True)
        hash_code = models.CharField(max_length=500, primary_key=True, default=_generateHash, unique=True, editable=False)

        def save(self):
                self.hash_code = self.role+'-'+self.hash_code+self.user_name
                super(User, self).save()
        
        def __str__(self):
                return self.hash_code
        
        def get_absolute_url(self):
                return reverse('usermanagement:user_edit', kwargs={'pk': self.pk})