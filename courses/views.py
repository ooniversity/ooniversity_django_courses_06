from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import logging

logger = logging.getLogger('courses')


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        logger.debug('Courses detail view has been debugged!')
        logger.info('Logger of courses detail view informs you!')
        logger.warning('Logger of courses detail view warns you!')
        logger.error('Courses detail view went wrong!')

        context = super().get_context_data(**kwargs)
        context['title'] = 'Course creation'
        lessons = Lesson.objects.filter(course=self.kwargs['pk'])
        context['lessons'] = lessons
        return context


class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/add.html'
    context_object_name = 'course'
    form_class = CourseModelForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course creation'
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        saved_form = form.save()
        messages.success(self.request,
                         'Course {} has been successfully added.'.format(saved_form.name))
        return response


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit.html'
    context_object_name = 'course'
    form_class = CourseModelForm

    def get_success_url(self):
        return reverse_lazy('courses:edit', args=(self.object.id, ))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course update'
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'The changes have been saved.')
        return response


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    context_object_name = 'course'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course deletion'
        return context

    def delete(self, request, *args, **kwargs):
        response = super().delete(self, request, *args, **kwargs)
        messages.success(self.request, 'Course {} has been deleted.'.format(self.object.name))
        return response


class LessonCreateView(CreateView):
    model = Lesson
    template_name = 'courses/add_lesson.html'
    context_object_name = 'lessons'
    form_class = LessonModelForm
    success_url = reverse_lazy('courses: detail')

    def get_success_url(self):
        return reverse_lazy('courses:detail', kwargs={'pk': self.object.course.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lesson creation'
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Lesson has been successfully added.')
        return response