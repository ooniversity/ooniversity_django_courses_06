from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from coaches.models import Coach
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django import forms
from django.core.urlresolvers import reverse

# Create your views here.

def detail(request, id):
    course = Course.objects.get(pk = int(id))
    lessons = Lesson.objects.filter(course_id = int(id)).order_by('order')
    return render(request, 'courses/detail.html', {'course': course, 'lessons': lessons})

def create(request):
	form = CourseModelForm(request.POST or None)
	if form.is_valid():
		course = form.save()
		messages.success(request, "Course %s has been successfully added." %(course.name))
		return redirect('index')
	return render(request, 'courses/add.html', {'form': form})

def remove(request, id):
	course = Course.objects.get(id = id)
	if request.method == "POST":
		coursename = course.name
		course.delete()
		messages.success(request, "Course %s has been deleted." %(course.name))
		return redirect('index')
	return render(request, 'courses/remove.html', {'course': course})

def edit(request, id):
	course = Course.objects.get(id = id)

	if request.method == "POST":
		form = CourseModelForm(request.POST, instance=course)
		if form.is_valid():
			course = form.save()
			messages.success(request, "The changes have been saved.")
			url_string = reverse('courses:edit', args=(id))
			print(url_string)
			return redirect(url_string)
		else:
			form = CourseModelForm(request.POST, instance=course)
    
	form = CourseModelForm(instance=course)
	return render(request, 'courses/edit.html', {'form': form})

def add_lesson(request, id):
	form = LessonModelForm(request.POST or None)
	if form.is_valid():
		form = form.save()
		print(form)
#		messages.success(request, "Lesson %s has been successfully added." %(lesson.name))
		url_string = reverse('courses:detail', args=(id))
		return redirect(url_string)
	return render(request, 'courses/add_lesson.html', {'form': form})	
