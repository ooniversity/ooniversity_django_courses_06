from django.contrib import admin
from coaches.models import *
from django.contrib.auth.models import User

# Register your models here.

class CoachAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'skype', 'description']
    list_filter = ['user__is_staff']


admin.site.register(Coach, CoachAdmin)
