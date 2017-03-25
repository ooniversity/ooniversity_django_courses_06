from django.db import models
from courses.models import Course

class Student(models.Model):
	name = models.CharField(max_length=254)
	surname = models.CharField(max_length=254)
	date_of_birth = models.DateField()
	email = models.EmailField()
	phone = models.CharField(max_length=254)
	address = models.CharField(max_length=254)
	skype = models.CharField(max_length=254)
	courses = models.ManyToManyField(Course)

	def __str__(self):
		return self.name

	def get_courses(self):
		return self.courses.all()
