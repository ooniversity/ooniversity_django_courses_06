#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import Coach
from courses.models import Course


def detail(request, coach_id):
    coach = Coach.objects.get(id=coach_id)
    course_coach = Course.objects.select_related().filter(coach=coach)
    course_assistant = Course.objects.select_related().filter(assistant=coach)
    return render(request, 'coaches/detail.html', {'coach': coach, 'course_coach': course_coach,
                                                   'course_assistant': course_assistant})
