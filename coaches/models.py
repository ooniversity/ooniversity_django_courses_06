from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=64, choices=(('M', 'Male'),('F', 'Female')))
    phone = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    skype = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.user.username
    
    def full_name(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)

    def name(self):
        return self.user.first_name

    def surname(self):
        return self.user.last_name
