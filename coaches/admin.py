from django.contrib import admin

from .models import Coach


class CoachesAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'gender', 'skype', 'description']
    list_filter = ['user__is_staff']

admin.site.register(Coach, CoachesAdmin)
