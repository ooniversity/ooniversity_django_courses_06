from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from django import forms
from django.contrib import messages
from courses.forms import CourseModelForm, LessonModelForm
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'

    def get_queryset(self):
        qs = super().get_queryset()
        cours_id = self.request.GET.get('pk', None)
        if cours_id:
            qs = qs.filter(courses=cours_id)
        return qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.filter(course=self.object.pk)
        #context['course'] = Course.objects.get(id=self.object.pk)
        return context

"""
def detail(request, course_id):
    lesson = Lesson.objects.filter(course=course_id)
    course = Course.objects.get(id=course_id)
    context = {'course': course, 'lessons': lesson}
    return render(request, "courses/detail.html", context)
"""
class CourseCreateView(CreateView):
    model = Course
    form_class = CourseModelForm
    template_name = 'courses/add.html'
    success_url = reverse_lazy('index')
    context_object_name = 'course'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Course %s has been successfully added.')
                          # %self.object.name or form.instance.name
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course creation'
        return context

"""        
def add(request):
    if request.method == "POST":
        form = CourseModelForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, "Course %s has been successfully added." %course.name) 
            return redirect('index')
    else:	
        form = CourseModelForm()
    return render(request, "courses/add.html", {'form': form})
"""

class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseModelForm
    template_name = 'courses/edit.html'
    context_object_name = 'course'

    def get_success_url(self):
        return reverse('courses:edit', args=(self.object.pk,))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'The changes have been saved.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course update'
        return context

"""
def edit(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            messages.success(request, "The changes have been saved.") 
            return redirect('courses:edit', course.id)
    else:
        form = CourseModelForm(request.POST, instance=course)
    form = CourseModelForm(instance=course)
    return render(request, 'courses/edit.html', {'form': form})
"""
class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    success_url = reverse_lazy('index')
    context_object_name = 'course'
    
    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Course has been deleted.') #self.object.name
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course deletion'
        return context

"""
def remove(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        course.delete()
        messages.success(request, "Course %s has been deleted." %course.name)
        return redirect('index')
    return render(request, 'courses/remove.html', {'course': course})

"""
def add_lesson(request, course_id):
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, "Lesson %s has been successfully added." %lesson.subject)
            return redirect('courses:detail', lesson.course.id)
    else:
        course = Course.objects.get(id=course_id)	
        form = LessonModelForm(initial={"course": course}) 
    return render(request, "courses/add_lesson.html", {'form': form})

