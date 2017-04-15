from django.db import models
from django.conf import settings
from courses.models import Course

class Student(models.Model):
    name=models.CharField(max_length=60)         
    surname=models.CharField(max_length=60)     
    date_of_birth=models.DateField()    
    email=models.EmailField()
    phone=models.CharField(max_length=15)   
    address=models.CharField(max_length=255)      
    skype=models.CharField(max_length=25)
    courses=models.ManyToManyField(Course)   

    def full_name(self):
        self.full_n = self.name + " " + self.surname
        return self.full_n
    def __str__(self):
        return self.full_name()
