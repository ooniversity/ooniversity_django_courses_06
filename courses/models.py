from __future__ import unicode_literals

from django.db import models
from coaches.models import Coach


class Course(models.Model):
    name = models.CharField(max_length=250)
    short_description = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    coach = models.ForeignKey(Coach, null=True, blank=True, on_delete=models.CASCADE,
                              related_name='coach_courses', )
    assistant = models.ForeignKey(Coach, null=True, blank=True, on_delete=models.CASCADE,
                                  related_name='assistant_courses', )

    def __str__(self):
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.subject
