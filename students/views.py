from django.shortcuts import render
from students.models import Student
from courses.models import Course

def list_view(request):
    if request.GET:
        students = Student.objects.filter(courses__id=int(request.GET['course_id']))
    else:
        students = Student.objects.all()
    for i in students:
        students_courses = Course.objects.all()
    return render(request, 'students/list.html', {'students_list': students, 'students_courses': students_courses})

def detail(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', {'student': student})
