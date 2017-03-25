from django.db import models

from courses.models import Course

class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    skype = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)

    def get_courses(self):
        return self.courses.all()
