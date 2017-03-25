from django.db import models


class Course(models.Model):
    name = models.CharField('Название',max_length=200)
    short_description = models.CharField('Кратное описание',max_length=200)
    description = models.TextField('Детальная информация')
    
    def __str__(self):
        return self.name

class Lesson(models.Model):
    subject = models.CharField('Тема',max_length=200)
    description = models.TextField('Описание')
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()
    def __str__(self):
        return self.subject 

    

# Create your models here.
