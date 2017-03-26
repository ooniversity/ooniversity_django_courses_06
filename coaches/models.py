from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Coach(models.Model):
    user = models.OneToOneField (User,on_delete=models.CASCADE)
    date_of_birth = models.DateField('Дата народження')
    gender = models.CharField('Стать',max_length=1,choices=(('M', 'Male'), ('F', 'Female')))
    phone = models.CharField('Тел',max_length=15)
    address = models.CharField('Адреса',max_length=25)
    skype = models.CharField(max_length=15)
    description  = models.TextField('Опис')
    
    def __str__(self):
        return str(self.user.username)


    def name(self):
        return self.user.first_name

    def surname(self):
        return self.user.last_name

'''    def e_mail(self):
        return self.user.email'''
