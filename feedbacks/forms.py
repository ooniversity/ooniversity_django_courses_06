from django import forms
from feedbacks.models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        #fields =  '__all__'
        fields = ['name', 'subject', 'message', 'from_email']