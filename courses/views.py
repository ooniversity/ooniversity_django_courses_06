from django.shortcuts import render
from courses.models import Course, Lesson


def detail(request, course_id_):
    course_ = Course.objects.filter(pk = int(course_id_))
    lessons = Lesson.objects.filter(course_id = int(course_id_))

    return render(request, 'courses/detail.html', {'course_': course_[0], 'lessons': lessons})


