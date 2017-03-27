from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Coach(models.Model):
    def __str__(self):
        return self.user.username

    def get_full_name(self):
        return self.user.first_name + ' ' + self.user.last_name


    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    phone = models.CharField(max_length=35)
    address = models.CharField(max_length=125)
    skype = models.CharField(max_length=25)
    description = models.TextField()
