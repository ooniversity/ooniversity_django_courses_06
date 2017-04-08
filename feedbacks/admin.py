from django.contrib import admin
from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm
from django.db import models
from django.forms import widgets 

# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('from_email', 'create_date')


admin.site.register(Feedback, FeedbackAdmin)
