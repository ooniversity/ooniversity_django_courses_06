from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from django import forms
from django.contrib import messages
from courses.forms import CourseModelForm, LessonModelForm

def detail(request, course_id):
	context = {'course': Course.objects.get(id=course_id), 'lessons': Lesson.objects.filter(course=course_id)}
	return render(request, "courses/detail.html", context)

def add(request):
	if request.method == "POST":
		form = CourseModelForm(request.POST)
		if form.is_valid():
			course = form.save()
			messages.success(request, "Course %s has been successfully added." % (course.name))
			return redirect('index')
	else:	
		form = CourseModelForm()
	return render(request, "courses/add.html", {'form': form})


def edit(request, course_id):
	course = Course.objects.get(id=course_id)
	if request.method == "POST":
		form = CourseModelForm(request.POST, instance=course)
		if form.is_valid():
			course = form.save()
			messages.success(request, "The changes have been saved.")
			return redirect('courses:edit', course.id)
	else:
		form = CourseModelForm(request.POST, instance=course)
	form = CourseModelForm(instance=course)
	return render(request, 'courses/edit.html', {'form': form})


def remove(request, course_id):
	course = Course.objects.get(id=course_id)
	if request.method == "POST":
		course.delete()
		messages.success(request, "Course %s has been deleted." % (course.name))
		return redirect('index')
	return render(request, 'courses/remove.html', {'course': course})


def add_lesson(request):
	if request.method == "POST":
		form = LessonModelForm(request.POST)
		if form.is_valid():
			lesson = form.save()
			messages.success(request, "Course %s has been successfully added." % (lesson.subject))
			return redirect('courses:detail', lesson.course.id)
	else:	
		form = LessonModelForm(initial={"course": course}) 
	return render(request, "courses/add_lesson.html", {'form': form})