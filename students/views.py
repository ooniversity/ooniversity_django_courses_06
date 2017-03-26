from django.shortcuts import render
from .models import Student

from courses.models import Course


def list_view(request):
    course_id = request.GET.get('course_id')
    courses = Course.objects.all()

    if course_id is not None:
        students = Student.objects.select_related()
        return render(request, 'students/list.html', {'students': students, 'courser': courses, 'course_id': course_id})
    else:
        students = Student.objects.all()
        return render(request, 'students/list.html', {'students': students, 'courser': courses})


def detail(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', {'student': student})
