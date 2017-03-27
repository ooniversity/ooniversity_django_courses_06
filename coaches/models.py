from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Coach(models.Model):
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))

    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=250, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    skype = models.CharField(max_length=250)
    description = models.TextField(blank=True)


    def __str__(self):
        return self.user.username

    def name(self):
        return self.user.first_name

    def surname(self):
        return self.user.last_name