from django.shortcuts import render

from . models import Student
from courses.models import Course



def list_view(request):
    data = request.GET

    if data:
        course_id = data['course_id']
        course = Course.objects.get(id=course_id)
        students_list = Student.objects.filter(courses__id=course_id)

        context = {
            'students_list': students_list,
            'current_course': course,
        }
    else:
        students_list = Student.objects.all()
        context = {
            'students_list': students_list
        }

    return render(request, 'students/list.html', context)


def detail(request, student_id):
    student = Student.objects.get(id=student_id)

    context = {
        'student': student
    }

    return render(request, 'students/detail.html', context)

def add(request,id):
	if request.method == 'POST':
		form = StudentModelForm(request.POST)
		if form.is_valid():
			student = form.save()
			message = u"Student %s %s has been successfully added." %(student.name, student.surname)
			messages.success(request, message)
			return redirect('students:list_view')
	else:
		form = StudentModelForm()

	return render(request, 'students/add.html', {'form':form})



 
