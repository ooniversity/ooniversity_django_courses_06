from django.db import models
from courses.models import Course
from datetime import date

class Student(models.Model):
    name = models.CharField(max_length=80)
    surname = models.CharField(max_length=80)
    date_of_birth = models.DateField(default=date.today)
    email = models.EmailField()
    phone = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    skype = models.CharField(max_length=64)
    courses = models.ManyToManyField(Course)

    def full_name(self):
        return ("%s %s" % (self.name, self.surname))

    def __str__(self):
        return self.name
