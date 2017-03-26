from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=15, choices=(('M', 'Male'), ('F','Female')))
    phone = models.CharField(max_length=150)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.user.username

    def first_name(self):
        return self.user.first_name
        
    def last_name(self):
        return self.user.last_name		
    def email(self):
        return self.user.email

