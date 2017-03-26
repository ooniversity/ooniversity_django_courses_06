from django.contrib import admin
from coaches.models import Coach
from django.contrib.auth.models import User

class CoachAdmin(admin.ModelAdmin):
        list_display = ['name', 'surname', 'gender', 'skype', 'description']
        list_filter = ['user__is_staff', 'user__is_active']
        list_display_links = ['name', 'surname']

admin.site.register(Coach, CoachAdmin)