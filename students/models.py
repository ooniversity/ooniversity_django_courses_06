from django.db import models
from courses.models import Course


class Student(models.Model):
    name = models.CharField(verbose_name=u'имя', max_length=64)
    surname = models.CharField(verbose_name=u'фамилия', max_length=64)
    date_of_birth = models.DateField(verbose_name=u'дата рождения', null=True, blank=True) 
    email = models.EmailField(unique=True, null=True )
    phone = models.CharField(verbose_name=u'телефон', max_length=15)
    address = models.CharField(verbose_name=u'адрес',max_length=255)
    skype = models.CharField(max_length=64)
    courses = models.ManyToManyField(Course, verbose_name=u'курсы, на которых учится студент')
    
    def __str__(self):
            return '%s %s' % (self.surname, self.name)
        


