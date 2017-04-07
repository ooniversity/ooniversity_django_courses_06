from django.shortcuts import render
from django.views.generic.edit import CreateView
from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm
from django.urls import reverse_lazy
from django.contrib import messages

class FeedbackView(CreateView):
    model = Feedback
    template_name = 'feedbacks/feedback.html'
    context_object_name = 'feedback'
    form_class = FeedbackForm
    success_url = reverse_lazy('feedbacks:feed-back')
    #success_url = reverse_lazy('index')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Feedback'
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        form.save()
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        return response


