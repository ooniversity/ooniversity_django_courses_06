from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from coaches.models import Coach
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Информация о курсе"
        context['lessons'] = Lesson.objects.filter(course_id=self.kwargs['pk'])
        return context

class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/add.html'
    form_class = CourseModelForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Course %s has been successfully added." %(self.object.name))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Course creation"
        return context

class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = 'courses/remove.html'

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(request, "Course %s has been successfully deleted." %(self.object.name))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Course deletion"
        return context


class CourseUpdateView(UpdateView):
    model = Course
    form_class =  CourseModelForm
    success_url = reverse_lazy('index')
    template_name = 'courses/edit.html'
    
#    def get_success_url(self, **kwargs):
#        print(self.kwargs)
#        return reverse_lazy('courses:edit', args = (self.kwargs['pk']))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Course %s info has been successfully changed." %(self.object.name))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Course update"
        context['coach'] = Lesson.objects.filter(course_id=self.kwargs['pk'])
        return context    

class LessonCreateView(CreateView):
    model = Lesson
    template_name = 'courses/add_lesson.html'
    form_class = LessonModelForm

    def get_initial(self):
        initial = super().get_initial()
        course = Course.objects.get(id=self.kwargs['id'])
        initial['course'] = course
        return initial

    def get_success_url(self, **kwargs):
        return reverse_lazy('courses:detail', args=(self.kwargs['id']))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Lesson has been successfully added.")
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Lesson creation"
        return context