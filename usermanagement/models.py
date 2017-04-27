from __future__ import unicode_literals
import datetime
from django.db import models, IntegrityError
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

        def save(self, *args, **kwargs):
                if not self.hash_code:
                        print 'no hash code'
                        self.hash_code = self.role+'-'+_generateHash()+self.email
                else:
                        print 'has hash code'
                success = False
                while not success:
                        try:
                                super(User, self).save(*args, **kwargs)
                                print self.hash_code
                        except IntegrityError:
                                raise
                        else:
                                success = True
        
                def __str__(self):
                        return self.hash_code
        
        def __str__(self):
                return self.hash_code
        
        def get_absolute_url(self):
                return reverse('usermanagement:user_edit', kwargs={'pk': self.pk})