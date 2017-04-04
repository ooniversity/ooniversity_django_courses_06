from django.db import models
from courses.models import Course
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True,null=True)
    phone = models.CharField(max_length=20)
    skype = models.CharField(max_length=30)
    courses = models.ManyToManyField(Course)
