from django.contrib import admin
from coaches.models import Coach
from django.contrib.auth.models import User

class CoachAdmin(admin.ModelAdmin):
	list_display = ['user', 'gender', 'skype', 'description']
	list_filter = ['is_active']

admin.site.register(Coach, CoachAdmin)
