from django.db import models
from courses.models import Course

class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course, related_name='course')
    
    def full_name(self):
        return self.name + ' ' + self.surname

    def __str__(self):
        return self.name
