from django.shortcuts import render
from courses.models import Course, Lesson

# Create your views here.

def detail(request, course_id):

    current_course = Course.objects.get(id=course_id)
    lessons = Lesson.objects.filter(course=current_course).order_by('order')

    context = {'course': current_course, 'lessons': lessons}
    return render(request, 'courses/detail.html', context)