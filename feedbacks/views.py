from django.shortcuts import render, redirect, reverse
from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.core.mail import mail_admins

# Create your views here.


class FeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedback')
    

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        mail_admins(self.object.subject, self.object.message, self.object.from_email)
        return response
