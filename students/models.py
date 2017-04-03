from django.db import models
from courses.models import Course

class Student(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    email = models.EmailField(null=True,unique=True)
    phone = models.CharField(max_length=20)
    skype = models.CharField(max_length=20)
    courses = models.ManyToManyField(Course)

