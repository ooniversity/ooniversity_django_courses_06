from django.contrib import admin

from . models import Course, Lesson

class LessonInline(admin.StackedInline):
    model = Lesson
    fields = ['subject', 'description', 'order']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_description']
    search_fields = ['name']
    inlines = [LessonInline]
    # list_filter = []
    # fields = ['name', 'description']
    # exclude = ['description']
    # readonly_fields = []

    # change widget
    # raw_id_fileds = []

    # buttons
    # save_as = True
    # save_on_top = True

    # fieldsets =

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
