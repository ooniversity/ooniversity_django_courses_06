from django.shortcuts import render
from students.models import Student
from courses.models import Course


def list_view(request):
    req = request.GET
    course_id = req.get('course_id', '')
    if course_id != '':
        course_students = Student.objects.filter(courses__id=course_id)
    else:
        course_students = Student.objects.all()
    return render(request, 'students/list.html', {
                           'students': course_students,	
                           })

def detail(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', {
                           'student': student,	
                           })
