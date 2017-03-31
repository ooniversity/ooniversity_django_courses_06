from django.shortcuts import render
from students.models import Student
from courses.models import Course


def list_view(request):
	if len(request.GET)>0:
		if request.GET['course_id']:
			studentsList = Student.objects.filter(courses__id=request.GET['course_id'])
		else:
			studentsList = Student.objects.all()
	else:
		studentsList = Student.objects.all()
	
	return render(request, 'students/list.html', {'studentsList': studentsList })

def detail(request, id):
    if request.method == 'GET':
        student = Student.objects.get(id = id)
    else:	
    	student = Student.objects.first()
    courses = Course.objects.all()
    return render(request, 'students/detail.html', {'student': student, 'courses' : courses})
