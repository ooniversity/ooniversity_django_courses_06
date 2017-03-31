from django.shortcuts import render
from courses.models import Course, Lesson
from coaches.models import Coach

# Create your views here.

def detail(request, id):
    course = Course.objects.get(pk = int(id))
    lessons = Lesson.objects.filter(course_id = int(id)).order_by('order')
    return render(request, 'courses/detail.html', {'course': course, 'lessons': lessons, 'coach': course.coach, 'assistant': course.assistant})


