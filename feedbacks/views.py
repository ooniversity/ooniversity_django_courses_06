from django.core.mail import send_mail, mail_admins
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'USERS FEEDBACK'
        return context