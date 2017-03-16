from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
		return self.user.username

    def __unicode__(self):
		return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Trampoline(models.Model):
    trampolineID = models.CharField(max_length=10, primary_key = True)
    broken = models.BooleanField()
    category = models.ForeignKey(Category)

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








