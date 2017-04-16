from django.contrib import admin

from . models import Coach

class CoachAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'get_surname', 'gender', 'skype', 'description']
    list_display_links = ['get_name', 'get_surname']
    list_filter = ['user__is_staff', 'user__is_active', 'gender']

admin.site.register(Coach, CoachAdmin)
