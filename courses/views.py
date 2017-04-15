from django.shortcuts import render, redirect, reverse
from . models import Course, Lesson
from coaches.models import Coach
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

import logging
logger = logging.getLogger(__name__) #pybursa.views


# Create your views here.
class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'courses/detail.html'

    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses__id=course_id)
                           
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.filter(course=self.object.pk)
        context['course'] = Course.objects.get(id=self.object.pk)
        logger.debug("Courses detail view has been debugged!")
        logger.info("Logger of courses detail view informs you!")
        logger.warning("Logger of courses detail view warns you!")
        logger.error("Courses detail view went wrong!")
        return context


'''def detail(request, course_id):
    
    course = Course.objects.get(id=course_id)
    lessons_list = Lesson.objects.filter(course=course)
    coach = Coach.objects.get(id=course.coach.id)
    assistant = Coach.objects.get(id=course.assistant.id)

    return render(request, "courses/detail.html", {'course':course, 'lessons_list': lessons_list, 'coach':coach, 'assistant':assistant}) '''


'''def add(request):
    
    if request.method == "POST":
        form = CourseModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            form.save()
            messages.success(request, 'Course {} has been successfully added.'.format(data['name']))
            return redirect('/')
    else:
        form = CourseModelForm()
        
    return render(request, "courses/add.html", {'form':form})'''


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseModelForm
    success_url = reverse_lazy('index')
    context_object_name = 'course'
    template_name = 'courses/add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course creation'
        #context['button_name'] = 'Add'
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Course {} has been successfully added.'.format(self.object.name))
        return response
    



'''def edit(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == "POST":
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            data = form.cleaned_data
            
            course.save()
            messages.success(request, 'The changes have been saved.')
            return redirect('courses:edit', pk)
    else:
        form = CourseModelForm(instance=course)

    
    
    return render(request, "courses/edit.html", {'form':form})'''


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseModelForm
    context_object_name = 'course'
    template_name = 'courses/edit.html' 

    def get_success_url(self):
        return reverse('courses:edit', args=(self.object.pk,))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course update'
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'The changes have been saved.')
        return response
    
    


'''def remove(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == "POST":
                
            course.delete()
            messages.success(request, 'Course {} has been deleted.'.format(course.name))
            return redirect('/')
    else:
        form = CourseModelForm(instance=course)

    
    
    return render(request, "courses/remove.html", {'form':form}) '''

    
class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')
    context_object_name = 'course'
    template_name = 'courses/remove.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course deletion'
        return context 

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Course {} has been deleted.'.format(self.object.name))
        return response       


def add_lesson(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == "POST":
        form = LessonModelForm(request.POST, initial = {'course':course.id})
        if form.is_valid():
            data = form.cleaned_data
            
            form.save()    
        messages.success(request, 'Lesson {} has been successfully added.'.format(data['subject']))
        return redirect('courses:detail', pk)


    else:
        form = LessonModelForm()
        
    return render(request, "courses/add_lesson.html", {'form':form})
