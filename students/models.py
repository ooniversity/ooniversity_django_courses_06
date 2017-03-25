from django.db import models
from courses.models import Course

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=180)
    surname = models.CharField(max_length=180)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=150)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=150)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name
    def fulname(self):
        return self.name + ' ' + self.surname
        #my_property.short_description = "Full name of the person"

    full_name = property(fulname)
