from django.contrib import admin
from coaches.models import Coach
from django.contrib.auth.models import User

# Register your models here.

class CoachAdmin(admin.ModelAdmin):
#	fields   = ['user', 'skype', 'description']
   list_display = ('name', 'surname', 'gender', 'skype', 'description')
   list_filter = ['user', 'user__is_staff']
   list_display_links = ['name', 'surname', 'skype',]

admin.site.register(Coach, CoachAdmin)