from django.contrib import admin
from courses.models import Course, Lesson


class LessonInline(admin.TabularInline):
    model = Lesson
    fields = ['subject', 'description', 'order']

class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "short_description"]
    inlines = [LessonInline]
    search_fields = ['name']


class LessonAdmin(admin.ModelAdmin):
    list_per_page = 5


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin) 
