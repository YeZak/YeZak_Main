from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings
from django.dispatch import receiver

class Account(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=20)  # Field name made lowercase.
    password = models.CharField(max_length=45)
    profile_pic = models.CharField(max_length=45, blank=True, null=True)
    name = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member'
    
class Member(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=20)  # Field name made lowercase.
    password = models.CharField(max_length=45)
    profile_pic = models.CharField(max_length=45, blank=True, null=True)
    name = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member'