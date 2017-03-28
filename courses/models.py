from django.db import models


class Course(models.Model):
    name = models.CharField(verbose_name=u'название', max_length=64)  
    short_description = models.CharField(verbose_name=u'краткое описание', max_length=255)  
    description = models.TextField(verbose_name=u'полное описание', null=True, blank=True)
    
    def __str__(self):
        return self.name  
    
    
class Lesson(models.Model):
    subject = models.CharField(verbose_name=u'тема', max_length=255)                    
    description = models.TextField(verbose_name=u'описание', null=True, blank=True)
    course = models.ForeignKey(Course, verbose_name=u'курс')
    order = models.PositiveIntegerField(verbose_name=u'номер по порядку') 

    def __str__(self):
        return self.subject      


