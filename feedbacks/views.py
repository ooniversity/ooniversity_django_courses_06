from django.shortcuts import render
from feedbacks.models import Feedback
from feedbacks.forms import FeedbackModelForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.core.mail import mail_admins

class FeedbackView(CreateView):
    model = Feedback
    template_name = 'feedback/feedback.html'
    context_object_name = 'feedback'
    form_class = FeedbackModelForm
#    success_message = "Thank you for your feedback! We will keep in touch with you very soon!"
    success_url = reverse_lazy('feedback')

    def form_valid(self, form):
        self.object = form.save()
        response = super().form_valid(form)
        sendMail = mail_admins(
            self.object.subject,
            self.object.message,
            self.object.from_email)
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Feedback creation"
        return context