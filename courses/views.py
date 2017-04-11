from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm

import logging
logger = logging.getLogger(__name__)
# Create your views here.

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html' 
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView,self).get_context_data(**kwargs)
        context['title'] = 'TechBursa Python/Django 06 :: CourseDetail'
        context['lessons'] = Lesson.objects.filter(course=self.kwargs['pk'])
        logger.debug('Уровень DEBUG: "Courses detail view has been debugged!"')
        logger.info('Уровень INFO: "Logger of courses detail view informs you!"')
        logger.warning('Уровень WARNING: "Logger of courses detail view warns you!"')
        logger.error('Уровень ERROR: "Courses detail view went wrong!"')
        return context


class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/add.html'
    form_class = CourseModelForm
    success_url = reverse_lazy('index')
    context_object_name = 'course'

    def form_valid(self, form):
        response = super(CourseCreateView, self).form_valid(form)
        messages.success(self.request, "Course {} has been successfully added.".format(self.object.name))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Course creation"
        return context


class CourseUpdateView(UpdateView):
    model = Course
    form_class =  CourseModelForm
    success_url = reverse_lazy('courses:edit')
    template_name = 'courses/edit.html'
    context_object_name = 'course'

    
    def get_success_url(self, **kwargs):
        return reverse_lazy('courses:edit', args = (self.kwargs['pk']))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "The changes have been saved.")
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Course update"
        return context


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = 'courses/remove.html'
    context_object_name = 'course'

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(request, "Course {} has been deleted.".format(self.object.name))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Course deletion"
        return context


class LessonCreateView(CreateView):
    model = Lesson
    template_name = 'courses/add_lesson.html'
    form_class = LessonModelForm
    context_object_name = 'lessons'
    success_url = reverse_lazy('courses:detail')

    def get_initial(self):
        initial = super().get_initial()
        course = Course.objects.get(id=self.kwargs['pk'])
        initial['course'] = course
        return initial

    def get_success_url(self, **kwargs):
        return reverse_lazy('courses:detail', args=(self.kwargs['pk']))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Lesson has been successfully added.")
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "ADD LESSON"
        return context
    
#--------------------------- old syntax ----------------

def add(request):
    if request.method == "POST":
        form = CourseModelForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, "Course {} has been successfully added.".format(course.name))
            return redirect('/')
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', {'form': form})


def edit(request, id):
    course = Course.objects.get(pk=id)
    if request.method == "POST":
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            messages.success(request, "The changes have been saved.")
            return redirect('courses:edit', id)
    form = CourseModelForm(instance=course)
    return render(request, 'courses/edit.html', {'form': form})

def remove(request, id):
        course = Course.objects.get(pk=id)
        if request.method == "POST":
            course.delete()
            messages.success(request, "Course {} has been deleted.".format(course.name))
            return redirect('/')
        return render(request, 'courses/remove.html', {'course': course})
    
def add_lesson(request, id):
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, "Lesson {} has been successfully added.".format(lesson.subject))
            return redirect('courses:detail', id)
    else:
        form = LessonModelForm(initial={'course':id})
    return render(request, 'courses/add_lesson.html', {'form': form})
    