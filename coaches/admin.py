from django.contrib import admin
from coaches.models import Coach
from django.contrib.auth.models import User

# Register your models here.

class CoachAdmin(admin.ModelAdmin):
    list_view = ['user', 'gender', 'skype', 'description']




admin.site.register(Coach, CoachAdmin)