from django.contrib import admin
from coaches.models import Coach
from django.contrib.auth.models import User

class CoachAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'gender', 'skype', 'description']
	list_filter = ['is_active', 'is_staff']

admin.site.register(Coach, CoachAdmin)
