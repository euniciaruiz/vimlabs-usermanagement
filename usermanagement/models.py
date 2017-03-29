from __future__ import unicode_literals
import datetime
from django.db import models

def _generateHash():
        return 'u-'+datetime.datetime.now().strftime("%Y%m%d%H%M%S")

# Create your models here.
class Manager(models.Model):
        user_name = models.CharField(max_length=200)
        email = models.CharField(max_length=200)
        hash_code = models.CharField(max_length=500, primary_key=True, default=_generateHash, unique=True, editable=False)

class User(models.Model):
        TESTER = 'T'
        DEVELOPER = 'D'

        ROLES = (
                        (TESTER, 'Tester'), 
                        (DEVELOPER, 'Developer'),
                )
        user_name = models.CharField(max_length=200)
        email = models.CharField(max_length=200)
        roles = models.CharField(max_length=1, choices=ROLES, null=True)    
        hash_code = models.CharField(max_length=500, primary_key=True, default=_generateHash, unique=True, editable=False)