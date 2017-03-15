from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
		return self.user.username

    def __unicode__(self):
		return self.user.username

class Trampoline(models.Model):
    trampolineID = models.CharField(max_length=10, primary_key = True)
    broken = models.BooleanField()
    category = models.CharField(max_length=20)

class Booking(models.Model):
    refNumber = models.IntegerField(primary_key = True)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    trampolineID = models.ForeignKey(Trampoline)
    userID = models.ForeignKey(User)

class Review(models.Model):
    revNumber = models.IntegerField(primary_key = True)
    time = models.DateField(auto_now=True)
    userID = models.ForeignKey(User)
    content = models.CharField(max_length=120)
    rating = models.IntegerField()





    
    
