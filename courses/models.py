from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=56)
    short_description = models.CharField(max_length=2000)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.name

class Lessons(models.Model):
    subject = models.CharField(max_length=56)
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.subject

