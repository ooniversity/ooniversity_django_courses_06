from django.db import models
import datetime

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100) # имя
    surname models.CharField(max_length=100) # фамилия
    date_of_birth = models.DateField() # дата рождения 
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20) # телефон
    address = models.CharField(max_length=200) # адрес
    skype = models.CharField(max_length=20)
    courses = models.ManyToManyField(courses.Course) # курсы студентa
    def __str__(self):
        return self.question_text
