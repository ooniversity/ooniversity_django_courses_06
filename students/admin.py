from django.contrib import admin
from students.models import Student
from courses.models import Course
from django.db import models
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

# Register your models here.

def upper_case_name(obj):
   return ("%s %s" % (obj.name, obj.surname))
upper_case_name.short_description = 'Full name'

class MembershipInline(admin.TabularInline):
    model = Student.courses.through

class CourseAdmin(admin.ModelAdmin):
    inlines = [MembershipInline, ]



class StudentAdmin(admin.ModelAdmin):
    search_fields = ['surname', 'email']
    list_display = [upper_case_name, 'email', 'skype']
    list_filter = ['courses']



    fieldsets = (
        ('Personal Info', {
            'fields': ('name', 'surname', 'date_of_birth')
        }),

        ('Contact Info', {
            'fields': ('email', 'phone', 'address', 'skype')
        }),

    )

    inlines = [MembershipInline, ]
    #exclude = ('courses',)
    #filter_horizontal = ['inlines']

    #formfield_override = {models.ModelMultiChoiceField: {'widget': widgets.TypedChoiceField} }


admin.site.register(Student, StudentAdmin)
#admin.site.register(Course)