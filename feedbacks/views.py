from django.shortcuts import render,redirect 
from django.shortcuts import render, redirect
from feedbacks.models import Feedback
from feedbacks.forms import FeedbackModelForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import mail_admins

class FeedbackView(SuccessMessageMixin, CreateView):
    model = Feedback
    template_name = 'feedback/feedback.html'
    form_class = FeedbackModelForm
    success_message = "Thank you for your feedback! We will keep in touch with you very soon!"
    success_url = 'feedback'

    def form_valid(self, form):
        self.object = form.save()
        data = form
        response = super().form_valid(form)
        sendMail = mail_admins(
        	self.object.subject,
        	self.object.message,
        	fail_silently=False)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Feedback creation"
        return context