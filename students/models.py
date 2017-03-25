from django.db import models
from django.conf import settings
from courses.models import *
from django.core.urlresolvers import reverse

class Student(models.Model):
	name = models.CharField('Имя', max_length=50)   # имя
	surname = models.CharField('Фамилия', max_length=50)  # фамилия
	date_of_birth = models.DateField('Дата рождения')# дата рождения 
	email = models.EmailField('e-mail')
	phone = models.CharField('Телефон', max_length=20)# телефон
	address = models.CharField('Адрес', max_length=200) # адрес
	skype = models.CharField('skype', max_length=20)
	courses = models.ManyToManyField(Course) # курсы, на которых учится студент
	def __str__(self):
            return self.name + " " + self.surname
	def Full_name(self):
	    return " ".join([self.name, self.surname])
	def get_courses(self):
	    return self.courses.all()

# Create your models here.
