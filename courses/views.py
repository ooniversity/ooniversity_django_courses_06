from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from django import forms
from django.contrib import messages


def detail(request, course_id):
    context = {'course': Course.objects.get(id=course_id), 
               'lessons': Lesson.objects.filter(course=course_id)}
    return render(request, "courses/detail.html", context)