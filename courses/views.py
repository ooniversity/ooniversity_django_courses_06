from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm

def detail(request, id):
    course = Course.objects.get(id=id)
    return render(request, 'courses/detail.html', {
                    'course': course,	
                    })

def add(request):
    context = {'error': False}
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            context['form'] = instance
            messages.success(request, "Course %s has been successfully added." %instance.name)
            return redirect('/')
    else:
        form = CourseModelForm()
    context['form'] = form
    return render(request, 'courses/add.html', context)

def edit(request, id):
    context = {'error': False}
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            instance = form.save()
            context['form'] = instance
            messages.success(request, "The changes have been saved." )
            return redirect('courses:edit', id=id)
    else:
        form = CourseModelForm(instance=course)
    context['form'] = form
    return render(request, 'courses/edit.html', context)

def remove(request, id):
    context = {'error': False}
    instance = Course.objects.get(id=id)
    if request.method == 'POST':
        messages.success(request, "Course %s has been deleted." %instance.name)
        instance.delete()
        return redirect('/')
    else:
        form = CourseModelForm(instance)
    context['course'] = instance
    context['form'] = form
    return render(request, 'courses/remove.html', context)

def add_lesson(request, id):
    context = {'error': False}
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            context['form'] = instance
            messages.success(request, "Lesson %s has been successfully added." %instance.subject)
            return redirect('courses:detail', id)
    else:
        form = LessonModelForm(initial={'course':id} )
    context['form'] = form
    return render(request, 'courses/add_lesson.html', context)
