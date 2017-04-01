from django.db import models
import datetime

# Create your models here.
class Student(models.Model):
    name = models.CharField("Ім’я", max_length=100)
    surname = models.CharField('Прізвище', max_length=100)
    date_of_birth = models.DateField('Дата народження',blank=True,null=True) 
    email = models.EmailField('e-mail',max_length=100,blank=True) 
    phone = models.CharField('№ тел.',max_length=20,blank=True) 
    address = models.CharField('Адреса',max_length=200,blank=True)
    skype = models.CharField(max_length=20,blank=True) 
    courses = models.ManyToManyField('courses.Course') 
    def __str__(self):
        return '%s %s' % (self.surname, self.name)
