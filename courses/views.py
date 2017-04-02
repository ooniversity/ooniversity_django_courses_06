from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from coaches.models import Coach
from django import forms
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages

def detail(request, course_id):
	course = Course.objects.get(id=course_id)
	lessons_list = Lesson.objects.filter(course=course_id)
	coach = Coach.objects.get(id=course.coach.id)
	assistant = Coach.objects.get(id=course.assistant.id)
	
	return render(request, 'courses/detail.html', {'course':course, 'lessons_list':lessons_list, 'coach':coach, 'assistant':assistant})

def add(request):
	if request.method == "POST":
		form = CourseModelForm(request.POST)
		if form.is_valid():
			course = form.save()
			messages.success(request, "Course {} has been successfully added.".format(course.name))
			return redirect('index')
	else:
		form = CourseModelForm()
	return render(request, 'courses/add.html', {'form': form})

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
		messages.success(request, "Course {} has been deleted.".format(course.name))
		return redirect('index')
	return render(request, 'courses/remove.html', {'course': course})

def add_lesson(request, course_id):
	if request.method == "POST":
		form = LessonModelForm(request.POST)
		if form.is_valid():
			lesson = form.save()
			messages.success(request, "Lesson {} has been successfully added.".format(lesson.subject))
			return redirect('courses:detail', lesson.course.id)
	else:
		course = Course.objects.get(id=course_id)
		form = LessonModelForm(initial={'course': course})
	return render(request, 'courses/add_lesson.html', {'form': form})
