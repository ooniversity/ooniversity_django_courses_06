from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm
from django.contrib import messages
from django import forms
from django.core.urlresolvers import reverse 

def list_view(request):
    if request.GET.get('course_id'):
        students = Student.objects.filter(courses__id='course_id')
    else:
        students = Student.objects.all()
    students_courses = Course.objects.all()
    return render(request, 'students/list.html', {'students_list': students, 'students_courses': students_courses})

def detail(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', {'student': student})

def create(request):
	if request.method == "POST":
		form = StudentModelForm(request.POST)
		if form.is_valid():
			student = form.save()
			print(student.name)
			messages.success(request, "Student %s %s has been successfully added." % (student.name, student.surname))
			return redirect('students:list_view')
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
			return redirect('students:list_view')
	else:
		form = StudentModelForm(request.POST, instance=student)
	form = StudentModelForm(instance=student)
	return render(request, 'students/edit.html', {'form': form})

def remove(request, student_id):
	student = Student.objects.get(id=student_id)
	if request.method == "POST":
		student.delete()
		messages.success(request, "Info on %s %s has been successfully deleted." % (student.name, student.surname))
		return redirect('students:list_view')
	return render(request, 'students/remove.html', {'student': student})