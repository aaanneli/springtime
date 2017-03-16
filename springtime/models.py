from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
		return self.user.username

    def __unicode__(self):
		return self.user.username

class Trampoline(models.Model):
    trampolineID = models.CharField(max_length=10, primary_key = True, unique = True)
    broken = models.BooleanField()
    category = models.CharField(max_length=20, null = False)

    def __str__(self):
		return self.trampolineID

    def __unicode__(self):
		return self.trampolineID

class Booking(models.Model):
    refNumber = models.IntegerField(primary_key = True, unique = True)
    startTime = models.DateTimeField(null = False)
    endTime = models.DateTimeField(null = False)
    trampolineID = models.ManyToManyField(Trampoline)
    userID = models.ManyToManyField(User)


class Review(models.Model):
    revNumber = models.IntegerField(primary_key = True, unique = True)
    time = models.DateField(auto_now=True)
    userID = models.ForeignKey(User)
    content = models.CharField(max_length=120)
    rating = models.IntegerField(null = False)

    def __str__(self):
		return self.content

    def __unicode__(self):
		return self.content

