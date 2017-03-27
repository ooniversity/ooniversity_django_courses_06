from django.shortcuts import render
from students.models import Student

# Create your views here.
def list_view(request):

    if len(request.GET) == 0:
        student_list = Student.objects.all()
    else:
        course_id = request.GET['course_id']
        student_list = Student.objects.filter(courses__id=course_id)

    context = {'students': student_list}
    return render(request, 'students/list.html', context)


def detail(request, student_id):

    current_student = Student.objects.get(id=student_id)
    context = {'student': current_student}
    return render(request, 'students/detail.html', context)