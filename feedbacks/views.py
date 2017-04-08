from django.shortcuts import render, redirect, get_object_or_404
from feedbacks.models import Feedback
from .forms import FeedbackForm
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from django.core.mail import send_mail
from django.conf import settings

class FeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedback')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request,
                         'Thank you for your feedback! We will keep in touch with you very soon!')
        send_mail(self.object.subject, self.object.message, self.object.from_email, settings.ADMINS)
        return response
