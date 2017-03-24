from django.contrib import admin

# Register your models here.
from .models import Course, Lesson

admin.site.register(Course) #, Lesson)
admin.site.register(Lesson)
