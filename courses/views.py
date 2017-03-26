from django.shortcuts import render
from courses.models import Course, Lesson
from coaches.models import Coach


def detail(request, course_num='1'):
    my_course = Course.objects.filter(id=int(course_num)).first()
    course_lessons = Lesson.objects.filter(course = my_course)
    course_coache = Coach.objects.filter(coach_courses = my_course).first()
    course_assist = Coach.objects.filter(assistant_courses = my_course).first()
    return render(request, 'courses/detail.html', {
                    'my_course': my_course,
                    'course_lessons': course_lessons,
                    'course_coache': course_coache,
                    'course_assist': course_assist,	
                    })

