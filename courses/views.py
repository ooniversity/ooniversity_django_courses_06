from django.shortcuts import render

from . models import Course, Lesson
from coaches.models import Coach

def detail(request, course_id):
    course = Course.objects.get(id=course_id)
    lessons_list = Lesson.objects.filter(course=course)
    coach = Coach.objects.get(id=course.coach.id)
    assistant = Coach.objects.get(id=course.assistant.id)

    context = {
        'course': course,
        'lessons_list': lessons_list,
        'coach': coach,
        'assistant': assistant,
    }
    return render(request, 'courses/detail.html', context)
