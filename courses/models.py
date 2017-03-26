from django.db import models
from coaches.models import Coach

class Course(models.Model):
	name = models.CharField(max_length=254) # название курса
	short_description = models.CharField(max_length=254) # краткое описание
	description = models.TextField() # полное описание
	coach = models.ForeignKey(Coach, null=True, related_name='coach_courses')
	assistant = models.ForeignKey(Coach, null=True, related_name='assistant_courses')

	def __str__(self): # функция возвращает название курса
		return self.name 

class Lesson(models.Model):
	subject = models.CharField(max_length=254) # тема
	description = models.TextField() # описание
	course = models.ForeignKey(Course) # курс
	order = models.PositiveIntegerField() # номер по порядку

	def __str__(self): # функция возвращает тему урока
		return self.subject
