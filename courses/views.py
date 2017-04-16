'''
    Courses module
'''

import logging

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from coaches.models import Coach

from . models import Course, Lesson
from . forms import CourseModelForm, LessonModelForm

LOGGER = logging.getLogger('courses')


class CourseDetailView(DetailView):
    '''
        Detail information about course
    '''

    model = Course

    template_name = 'courses/detail.html'

    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        LOGGER.debug('Courses detail view has been debugged!')
        LOGGER.info('Logger of courses detail view informs you!')
        LOGGER.warning('Logger of courses detail view warns you!')
        LOGGER.error('Courses detail view went wrong!')

        context = super().get_context_data(**kwargs)

        context['lessons_list'] = Lesson.objects.filter(course=self.kwargs['pk'])

        return context


class CourseCreateView(CreateView):
    '''
        Create new course functionality
    '''

    model = Course

    form_class = CourseModelForm

    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)

        data = form.cleaned_data

        message = ('Course {} has been successfully added.'
                   .format(data['name']))

        messages.success(self.request, message)

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Course creation'
        context['button_text'] = 'Create'

        return context


class CourseUpdateView(UpdateView):
    '''
        Update course information functionality
    '''

    model = Course

    form_class = CourseModelForm

    def get_success_url(self):
        return reverse('courses:edit', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        response = super().form_valid(form)

        message = ('The changes have been saved.')

        messages.success(self.request, message)

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Course update'
        context['button_text'] = 'Update'

        return context


class CourseDeleteView(DeleteView):
    '''
        Delete course functionality
    '''

    model = Course

    success_url = reverse_lazy('index')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)

        course = self.object

        message = 'Course {} has been deleted.'.format(course.name)

        messages.success(self.request, message)

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Course deletion'

        return context


def add_lesson(request, course_id):
    '''
        Add new lesson functionality
    '''

    course = Course.objects.get(id=course_id)

    if request.method == 'POST':
        form = LessonModelForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            form.save()

            message = ('Lesson {} has been successfully added.'
                       .format(data['subject']))

            messages.success(request, message)

            return redirect('/courses/{}'.format(data['course'].id))
    else:
        form = LessonModelForm(initial={'course': course})

    context = {
        'form': form,
    }

    return render(request, 'courses/add_lesson.html', context)
