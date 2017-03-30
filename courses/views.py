from django.shortcuts import render
from courses.models import Course
# from coaches.models import Coach


# Create your views here.
def detail(request, id):
    course = Course.objects.get(pk=id)
    lessons = course.lesson_set.all()
    return render(request, 'courses/detail.html', {
                  'course': course,
                  'lessons': lessons,
                  'coach': course.coach,
                  'assistant': course.assistant, })
