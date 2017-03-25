from django.shortcuts import render
from . models import Student
from courses.models import Course

# Create your views here.
def list_view(request):
    data = request.GET
    course = None
    if data:
        course_id = data['course_id']
        course = Course.objects.get(id=course_id)
        students_list = Student.objects.filter(courses__id=course_id)
    else:
        students_list = Student.objects.all()
    
    return render(request, 'students/list.html', {'students_list':students_list, 'current_course': course})

def detail(request, student_id):
    student = Student.objects.get(id=student_id)

    return render(request, 'students/detail.html', {'student': student})
