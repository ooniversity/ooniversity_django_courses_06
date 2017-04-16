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


def list_view(request):
    data = request.GET

    if data:
        course_id = data['course_id']
        course = Course.objects.get(id=course_id)
        students_list = Student.objects.filter(courses__id=course_id)

        context = {
            'students_list': students_list,
            'current_course': course,
        }
    else:
        students_list = Student.objects.all()
        context = {
            'students_list': students_list
        }

    return render(request, 'students/list.html', context)


def detail(request, student_id):
    student = Student.objects.get(id=student_id)

    context = {
        'student': student
    }

    return render(request, 'students/detail.html', context)


def create(request):
    '''
        Create student functionality
    '''

    if request.method == 'POST':
        form = StudentModelForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            form.save()

            message = ('Student {} {} has been successfully added.'
                       .format(data['name'], data['surname']))

            messages.success(request, message)

            return redirect('/students/')
    else:
        form = StudentModelForm()

    context = {
        'form': form,
    }

    return render(request, 'students/add.html', context)


def edit(request, student_id):
    '''
        Edit student's information
    '''

    student = Student.objects.get(id=student_id)

    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)

        if form.is_valid():
            student = form.save()

            message = 'Info on the student has been successfully changed.'

            messages.success(request, message)

            return redirect('/students/edit/{}'.format(student_id))
    else:
        form = StudentModelForm(instance=student)

    context = {
        'form': form
    }

    return render(request, 'students/edit.html', context)


def remove(request, student_id):
    '''
        Remove student functionality
    '''

    student = Student.objects.get(id=student_id)

    if request.method == 'POST':
        message = ('Info on {} {} has been successfully deleted.'
                   .format(student.name, student.surname))

        student.delete()

        messages.success(request, message)

        return redirect('/students/')

    context = {
        'student': student
    }

    return render(request, 'students/remove.html', context)
