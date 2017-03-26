from django.contrib import admin
from students.models import Student
from courses.models import Course

class StudentAdmin(admin.ModelAdmin):


    search_fields = ['surname', 'email']
    list_display = [ 'fulname', 'email', 'skype']
    list_display_links = [ 'fulname',]
    list_filter = ['courses']
    filter_horizontal = ['courses', ]

    fieldsets = (
        ('Personal info', {
            'fields': ('name', 'surname', 'date_of_birth')
        }),

        ('Contact info', {
            'fields': ('email', 'phone', 'address', 'skype')
        }),

        (None, {'fields': ['courses']})
    )






# Register your models here.
admin.site.register(Student, StudentAdmin)
