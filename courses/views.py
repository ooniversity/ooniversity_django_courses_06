from django.shortcuts import render
from courses.models import Course, Lesson


def detail(request, pk):
    context = {'course': Course.objects.get(id=pk), 
               'lessons': Lesson.objects.filter(course=pk)}
    return render(request, "courses/detail.html", context)
