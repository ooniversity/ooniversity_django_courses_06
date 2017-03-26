from django.shortcuts import render
from students.models import Student
from courses.models import Course


def list_view(request):
    req = request.GET
    course_id = req.get('course_id', '')
    if course_id != '':
        my_students = Student.objects.filter(courses=Course.objects.filter(id=int(course_id)))
    else:
        my_students = Student.objects.all()
    return render(request, 'students/list.html', {
                    'students': my_students,	
				    })


def detail(request, student_id):
    student = Student.objects.filter(id=int(student_id)).first()
    return render(request, 'students/detail.html', {
				    'student': student,	
				    })
