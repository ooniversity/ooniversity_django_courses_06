from django.contrib import admin
from students.models import Student
from courses.models import Course

class StudentAdmin(admin.ModelAdmin):
	list_display = ['full_name', 'email', 'skype']
#	list_display_links = ['fulname',]
	fieldsets = (
		('Personal info', {
			'fields': ('name', 'surname', 'date_of_birth')
		}), 
		('Contact info', {
			'fields': ('email', 'phone', 'address', 'skype')
		}),
		(None, {
			'fields': ('courses',)
		}),
	)
	search_fields = ['surname', 'email']
	list_filter = ['courses']
	filteer_horizontal = ['courses',]

admin.site.register(Student, StudentAdmin)
