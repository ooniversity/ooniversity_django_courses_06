from django.contrib import admin
from feedbacks.models import *
# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
	model = Feedback
	list_display = [ 'from_email', 'create_date']


admin.site.register(Feedback, FeedbackAdmin)

