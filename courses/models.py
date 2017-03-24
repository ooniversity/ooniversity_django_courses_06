from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField('Назва', max_length=100)     # название
    short_description = models.CharField('Опис',max_length=200)     # краткое описание
    description = models.TextField('Детальна інформація')      # полное описание
    def __str__(self):
        return self.name
    
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE) # курс
    subject = models.CharField('Тема',max_length=200) # тема
    description = models.TextField('Опис') # описание
    order = models.PositiveIntegerField('№ п.п.') # номер по порядку 
    def __str__(self):
        return self.subject

