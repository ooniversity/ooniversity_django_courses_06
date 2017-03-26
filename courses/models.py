from django.db import models
from coaches.models import Coach

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)     # название
    short_description = models.CharField(max_length=200)     # краткое описание
    description = models.TextField()      # полное описание
    coach = models.ForeignKey(Coach, null=True, related_name='coach_courses')
    assistant = models.ForeignKey(Coach, null=True, related_name='assistant_courses')
    def __str__(self):
        return '%s' % (self.name)
    
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE) # курс
    subject = models.CharField(max_length=200) # тема
    description = models.TextField() # описание
    order = models.PositiveIntegerField() # номер по порядку 
    def __str__(self):
        return self.subject

