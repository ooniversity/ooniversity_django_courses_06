from django.contrib import admin

from django.contrib import admin
from feedbacks.models import Feedback
from django.contrib.auth.models import User


class FeedbackAdmin(admin.ModelAdmin):
   list_display = ('from_email', 'create_date')
#   list_filter = ['name', 'create_date']


admin.site.register(Feedback, FeedbackAdmin)