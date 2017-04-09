from django.contrib import admin
from feedbacks.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
	listdisplay = ['from_email', 'create_date']


admin.site.register(Feedback, FeedbackAdmin)
