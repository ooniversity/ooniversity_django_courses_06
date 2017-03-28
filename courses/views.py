from django.shortcuts import render
from courses.models import Course

def detail(request, course_num):
    course = Course.objects.get(id=course_num)
    return render(request, 'courses/detail.html', {
                    'course': course,	
                    })

