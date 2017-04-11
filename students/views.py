from django.shortcuts import render, redirect
from students.models import Student
from students.forms import StudentModelForm
from courses.models import Course
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import logging

logger = logging.getLogger('students')

class StudentListView(ListView):
    model = Student
    paginate_by = 2
    global_course_id = None
    trigger = None

    def get_queryset(self):
        global global_course_id
        global trigger
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            global_course_id = self.request.GET.get('course_id', None)
            trigger = True
        if self.request.GET.get('page', None) and trigger:
            qs = qs.filter(courses__id=global_course_id)
        elif course_id:
            qs = qs.filter(courses__id=course_id)
        else:
            trigger = False
        return qs

class StudentDetailView(DetailView):
    model = Student
    def get_context_data(self, **kwargs):
        logger.debug('Students detail view has been debugged!')
        logger.info('Logger of students detail view informs you!')
        logger.warning('Logger of students detail view warns you!')
        logger.error('Students detail view went wrong!')

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student registratio'
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Student has been successfully added.')
        return response

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Info on the student has been successfully changed.')
        return response

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        return context

    def delete(self, request, *args, **kwargs):
        response = super().delete(self, request, *args, **kwargs)
        messages.success(self.request, 'Info has been successfully deleted.')
        return response
