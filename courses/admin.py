from django.contrib import admin
from courses.models import Course, Lesson


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 0   
    
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description')
    search_fields = ['name']
    inlines = [LessonInline]
    
class LessonAdmin(admin.ModelAdmin):
    list_per_page = 10


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
