from django.shortcuts import render, redirect, reverse
from . models import Course, Lesson
from coaches.models import Coach
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



# Create your views here.
class CourseDetailView(DetailView):
	model = Course



'''def detail(request, course_id):
    
    course = Course.objects.get(id=course_id)
    lessons_list = Lesson.objects.filter(course=course)
    coach = Coach.objects.get(id=course.coach.id)
    assistant = Coach.objects.get(id=course.assistant.id)

    return render(request, "courses/detail.html", {'course':course, 'lessons_list': lessons_list, 'coach':coach, 'assistant':assistant}) '''


def add(request):
    
    if request.method == "POST":
        form = CourseModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            form.save()
            messages.success(request, 'Course {} has been successfully added.'.format(data['name']))
            return redirect('/')
    else:
        form = CourseModelForm()
        
    return render(request, "courses/add.html", {'form':form})


def edit(request, pk):
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

    
    
    return render(request, "courses/edit.html", {'form':form})

def remove(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == "POST":
                
            course.delete()
            messages.success(request, 'Course {} has been deleted.'.format(course.name))
            return redirect('/')
    else:
        form = CourseModelForm(instance=course)

    
    
    return render(request, "courses/remove.html", {'form':form})
    
    


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
