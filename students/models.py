from django.db import models
from courses.models import Course


class Student(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    date_of_birth = models.DateField(null=True, blank=True) 
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=64)
    courses = models.ManyToManyField(Course, help_text='Hold down "Control",or "Command" on a Mac, to select more then one.')
    
    def __str__(self):
            return '%s %s' % (self.surname, self.name)
        


