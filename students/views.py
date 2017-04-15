'''
    Students module
'''

import logging

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from courses.models import Course

from . models import Student
from . forms import StudentModelForm

LOGGER = logging.getLogger('students')


class StudentListView(ListView):
    '''
        List of students functionality
    '''

    model = Student

    def _get_course_id(self):
        return self.request.GET.get('course_id', None)

    def get_queryset(self):
        qs = super().get_queryset()

        course_id = self._get_course_id()

        if course_id:
            qs = qs.filter(courses__id=course_id)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        course_id = self._get_course_id()

        if course_id:
            context['current_course'] = Course.objects.get(id=course_id)

        return context


class StudentDetailView(DetailView):
    '''
        Detail information about student
    '''

    model = Student

    def get_context_data(self, **kwargs):
        LOGGER.debug('Students detail view has been debugged!')
        LOGGER.info('Logger of students detail view informs you!')
        LOGGER.warning('Logger of students detail view warns you!')
        LOGGER.error('Students detail view went wrong!')

        context = super().get_context_data(**kwargs)

        return context


class StudentCreateView(CreateView):
    '''
        Create student functionality
    '''

    model = Student

    form_class = StudentModelForm

    success_url = reverse_lazy('students:list_view')

    def form_valid(self, form):
        response = super().form_valid(form)

        data = form.cleaned_data

        message = ('Student {} {} has been successfully added.'
                   .format(data['name'], data['surname']))

        messages.success(self.request, message)

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Student registration'
        context['button_text'] = 'Create'

        return context


class StudentUpdateView(UpdateView):
    '''
        Update student information functionality
    '''

    model = Student

    form_class = StudentModelForm

    # success_url = reverse_lazy('students:edit')

    def get_success_url(self):
        return reverse('students:edit', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        response = super(StudentUpdateView, self).form_valid(form)

        message = ('Info on the student has been successfully changed.')

        messages.success(self.request, message)

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Student info update'
        context['button_text'] = 'Update'

        return context


class StudentDeleteView(DeleteView):
    '''
        Delet student functionality
    '''

    model = Student

    success_url = reverse_lazy('students:list_view')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)

        student = self.object

        message = ('Info on {} {} has been successfully deleted.'
                   .format(student.name, student.surname))

        messages.success(self.request, message)

        return response
