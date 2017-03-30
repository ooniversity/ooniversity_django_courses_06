from django.db import models
from django.contrib.auth.models import User

class Coach(models.Model):
	user = models.OneToOneField(User)#, on_delete=models.CASCADE)
	date_of_birth = models.DateField(null=True, blank=True)
	gender = models.CharField(max_length=254, choices=(('M', 'Male'), ('F', 'Female')))
	phone = models.CharField(max_length=254)
	address = models.CharField(max_length=254)
	skype = models.CharField(max_length=254)
	description = models.TextField()

	def __str__(self):
		return self.user.username

	def first_name(self):
		return self.user.first_name

	def last_name(self):
		return self.user.last_name

	def full_name(self):
		return self.user.first_name + ' ' + self.user.last.name	
