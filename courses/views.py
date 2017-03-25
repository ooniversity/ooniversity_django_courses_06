from django.shortcuts import render
from . models import Course, Lesson

# Create your views here.

def detail(request, course_id):
    
    course = Course.objects.get(id=course_id)
    lessons_list = Lesson.objects.filter(course=course)

    return render(request, "courses/detail.html", {'course':course, 'lessons_list': lessons_list})
