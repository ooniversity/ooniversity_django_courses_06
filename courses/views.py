from django.shortcuts import render
from courses.models import Course, Lesson

def detail(request, course_num='1'):
    my_course = Course.objects.filter(id=int(course_num)).first()
    course_lessons = Lesson.objects.filter(course = my_course)
    return render(request, 'courses/detail.html', {
				    'my_course': my_course,
                    'course_lessons': course_lessons,	
				    })

