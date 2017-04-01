from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course
from django import forms
from students.forms import StudentModelForm
from django.contrib import messages

def list_view(request):
	data = request.GET
	course = None
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

def create(request):
	if request.method == "POST":
		form = StudentModelForm(request.POST)
		if form.is_valid():
			student = form.save()
			messages.success(request, "Student {} {} has been successfully added.".format(student.name, student.surname))
			return redirect('/students/')
	else:
		form = StudentModelForm()
	return render(request, 'students/add.html', {'form': form})

def edit(request, student_id):
	student = Student.objects.get(id=student_id)
	if request.method == "POST":
		form = StudentModelForm(request.POST, instance=student)
		if form.is_valid():
			student = form.save()
			messages.success(request, "Info on the student has been successfully changed.")
			return redirect('/students/')
	else:
		form = StudentModelForm(request.POST, instance=student)
	form = StudentModelForm(instance=student)
	return render(request, 'students/edit.html', {'form': form})

def remove(request, student_id):
	student = Student.objects.get(id=student_id)
	if request.method == "POST":
		student.delete()
		messages.success(request, "Info on {} {} has been successfully deleted.".format(student.name, student.surname))
		return redirect('/students/')
	return render(request, 'students/remove.html', {'student': student})
