from django.contrib import admin
from courses.models import Course, Lesson

class LessonInline(admin.StackedInline):
	model = Lesson
	fields = ['subject', 'description', 'order']

class LessonAdmin(admin.ModelAdmin):
	pass

class CourseAdmin(admin.ModelAdmin):
	list_display = ['name', 'short_description']
	search_fields = ['name']
	inlines = [LessonInline]

#class LessonInline

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
