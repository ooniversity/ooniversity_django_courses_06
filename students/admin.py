from django.contrib import admin
from students.models import *

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['Full_name', 'email', 'skype']
    search_fields = ['surname', 'email']
    filter_horizontal = ['courses']
    fieldsets = [
        ('Personal info', {'fields': ['name', 'surname', 'date_of_birth']}),
        ('Contact info', {'fields': ['email', 'phone', 'address', 'skype']}),
        (None, {'fields': ['courses']})
            ]
    

admin.site.register(Student, StudentAdmin)
