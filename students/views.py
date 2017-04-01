from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm
from django.contrib import messages


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

def create(request):
	form = StudentModelForm(request.POST or None)
	if form.is_valid():
		student = form.save()
		messages.success(request, "Student {} {} has been successfully added.".format(student.name, student.surname))
		return redirect('/students/')
	return render(request, 'students/add.html', {'form': form})

def remove(request, id):
	student = StudentModelForm.objects.get(id = id)
	if request.method == "POST":
		studentname = student.full_name
		student.delete()
		message.success(request, "Student "+studentname+" was deleted")
		return redirect('/students/')
	return render(request, 'students/remove.html', {'student': student})

def edit(request, id):
	student = StudentModelForm.objects.get(id = id)
	if request.method == "POST":
		form = StudentModelForm(request.POST, instance=student)
		if form.is_valid():
			student = form.save()
			messages.success(request, "Изменения сохранены.")
			return redirect('/students/')
		else:
			form = StudentModelForm(request.POST, instance=student)
    
	form = StudentModelForm(instance=student)
	return render(request, 'students/edit.html', {'form': form})

	
