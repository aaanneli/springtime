from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
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

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural= 'Categories'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Trampoline(models.Model):
    trampolineID = models.CharField(max_length=8, primary_key = True, unique = True)
    broken = models.BooleanField(default = False)
    category = models.ForeignKey(Category, null = True)

    def __str__(self):
        return self.trampolineID

    def __unicode__(self):
        return self.trampolineID

class Booking(models.Model):
    refNumber = models.IntegerField(primary_key = True, unique = True)
    startTime = models.DateTimeField(null = False, auto_now=True)
    trampolineID = models.ManyToManyField(Trampoline)
    userID = models.ManyToManyField(User)

    def __str__(self):
        return str(self.refNumber)

    def __unicode__(self):
        return unicode(self.refNumber)

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