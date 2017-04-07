from django.shortcuts import render
from django.views.generic.edit import CreateView
from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import mail_admins

class FeedbackView(CreateView):
    model = Feedback
    template_name = 'feedbacks/feedback.html'
    context_object_name = 'feedback'
    form_class = FeedbackForm
    success_url = reverse_lazy('feedback')
    #success_url = reverse_lazy('index')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Feedback'
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        #print('FEEDBACK_1:', self.object.name)
        #print('FEEDBACK_1:', self.object.subject)
        #print('FEEDBACK_1:', self.object.message)
        #print('FEEDBACK_1:', self.object.from_email)
        mail_admins(self.object.subject, self.object.message, self.object.from_email)
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        return response
