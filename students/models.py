from django.db import models
from django.conf import settings
from courses.models import Course

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=35)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=70)
    skype = models.CharField(max_length=15)
    courses = models.ManyToManyField(Course)
    def full_name(self):
        self.full_n = self.name + " " + self.surname
        return self.full_n
    def __str__(self):
        return self.full_name()
