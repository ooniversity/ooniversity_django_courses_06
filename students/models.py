from __future__ import unicode_literals

from django.db import models

from courses.models import Course


class Student(models.Model):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    skype = models.CharField(max_length=250)
    courses = models.ManyToManyField(Course)
