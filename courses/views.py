#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import Course, Lesson
from coaches.models import Coach


def index(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {'courses': courses})


def detail(request, course_id):
    course = Course.objects.get(id=course_id)
    lessons = Lesson.objects.select_related().filter(course=course_id)
    print(course)

    return render(request, 'courses/detail.html', {'course': course, 'lessons': lessons})
